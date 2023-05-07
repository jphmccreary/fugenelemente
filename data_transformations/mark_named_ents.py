import dill as pickle
import spacy
import re
import sys
import os
from collections import defaultdict

print(os.getpid())

nlp = spacy.load('de_core_news_sm', disable=['tok2vec', 'morphologizer', 'parser', 'senter', 'attribute_ruler'])

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
                    yc.ent_types = defaultdict(int)

                ent_type = token.ent_type_

                yc.ent_types[ent_type] += 1

        print(f' {year}: {str(100 * count / len(sents))[:6]}%', end='\r')
        sys.stdout.flush()

    with open(f'dumps/spacy_attrs_added/{year}ycs', 'wb') as outfile:
        pickle.dump(ycs, outfile)

