import spacy
from space_tokenizer import WhitespaceTokenizer
import dill as pickle
import datetime
import os

print('pid: ' + str(os.getpid()))
nlp = spacy.load('de_core_news_sm')
nlp.tokenizer = WhitespaceTokenizer(nlp.vocab)

class YearedCompound:
    def __init__(self, source_yc):
        self.is_compound = source_yc.is_compound
        self.text = source_yc.text
        self.year = source_yc.year
        self.count = source_yc.count
        self.corpus = source_yc.corpus
        self.source = source_yc.source
        self.splits = source_yc.splits

    def add_lemmas(self, lemmas: tuple) -> None:
        self.lemmas = lemmas

# size of input in tokens
string_size = 1000

for year in range(1995, 2023):
    old_ycs = pickle.load(open(f'dumps/spaces_filtered/{year}ycs', 'rb'))
    ycs = [YearedCompound(yc) for yc in old_ycs]

    for i in range(0, len(ycs), string_size):
        t1 = datetime.datetime.now()
        one_string_list = []
        for j in range(i, i + string_size):
            if j >= len(ycs):
                break
            one_string_list.append(' '.join(ycs[j].splits))
        one_string = ' '.join(one_string_list)
        doc = nlp(one_string)
        lemmas = [token.lemma_ for token in doc]

        j = i # this copies the value right?
        k = 0
        while j < i + string_size:
            if j >= len(ycs):
                break
            split_count = len(ycs[j].splits)
            current_lemmas = tuple(lemmas[k:k+split_count])
            current_word = ycs[j].text
            # print(f'{current_word} | {current_lemmas}')

            ycs[j].add_lemmas(current_lemmas)

            j += 1
            k += split_count
        t2 = datetime.datetime.now()
        print(str(i) + ' ' + str(t2 - t1))

    pickle.dump(ycs, open(f'dumps/lemmatized/{year}ycs', 'wb'))
