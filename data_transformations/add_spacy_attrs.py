import dill as pickle
import spacy
import re
import sys
from numpy import array_equal
import os

print(os.getpid())

nlp = spacy.load('de_core_news_sm', disable=['morphologizer', 'parser', 'senter', 'attribute_ruler'])

separator = re.compile('^([0-9]+)\s+([^\n]+)')

for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/no_cooc_filtered/{year}ycs', 'rb'))
    sents_file = open(f'dumps/filtered_sents/{year}sents.txt')
    sents = [separator.search(line).group(2) for line in sents_file.readlines()]
    sents = tuple(sents)
    count = 0
    for doc in nlp.pipe(sents):
        count += 1
        for token in doc:
            text = token.text
            if text in ycs:
                # should be fine bc YearedCompound is a mutable type? (frozen=False)?
                yc = ycs[text]

                if not hasattr(yc, 'ent_types'):
                    yc.ent_types = []
                if not hasattr(yc, 'vectors'):
                    yc.vectors = []
                if not hasattr(yc, 'whole_lemmas'):
                    yc.whole_lemmas = []
                if not hasattr(yc, 'parts_of_speech'):
                    yc.parts_of_speech = []

                ent_type = token.ent_type_
                vector = token.vector
                whole_lemma = token.lemma_
                pos = token.pos_
                is_oov = token.is_oov

                if ent_type not in yc.ent_types:
                    yc.ent_types.append(ent_type)

                matching_vector_found = False
                for v in yc.vectors:
                    if array_equal(v, vector):
                        matching_vector_found = True
                        break
                if not matching_vector_found:
                    yc.vectors.append(vector)

                if whole_lemma not in yc.whole_lemmas:
                    yc.whole_lemmas.append(whole_lemma)

                if pos not in yc.parts_of_speech:
                    yc.parts_of_speech.append(pos)

                yc.is_oov = is_oov
        print(f' {year}: {str(100 * count / len(sents))[:6]}%', end='\r')
        sys.stdout.flush()

    with open(f'dumps/spacy_attrs_added/{year}ycs', 'wb') as outfile:
        pickle.dump(ycs, outfile)

