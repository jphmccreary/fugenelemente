import os
from datetime import datetime
import dill as pickle
from unfuge import operations

print('pid: ' + str(os.getpid()))

class YearedCompound:
    def __init__(self, source_yc):
        self.is_compound = source_yc.is_compound
        self.text = source_yc.text
        self.year = source_yc.year
        self.count = source_yc.count
        self.corpus = source_yc.corpus
        self.source = source_yc.source
        self.splits = source_yc.splits
        self.lemmas = source_yc.lemmas

        fuge_candidates_l = []
        lemma_matches_l = []

        for i, split in enumerate(self.splits[:-1]):
            fuge_candidates_l.append({})
            lemma_matches_l.append({})
            for key, op in operations.items():
                unfuged = op(split)
                if unfuged[1]:
                    fuge_candidates_l[i][key] = unfuged[0]
                    if unfuged[0].lower() == self.lemmas[i].lower():
                        lemma_matches_l[i][key] = unfuged[0]

        self.fuge_candidates = tuple(fuge_candidates_l)
        self.lemma_matches = tuple(lemma_matches_l)


def load_year(year):
    t1 = datetime.now()
    ycs = pickle.load(open(f'dumps/numbers_filtered/{year}ycs', 'rb'))
    t2 = datetime.now()
    elapsed = t2 - t1
    print(f'time to load {year}: {elapsed}')
    return ycs

for year in range(2001, 2023):
    old_ycs = load_year(year)
    ycs = []

    t1 = datetime.now()
    for yc in old_ycs:
        ycs.append(YearedCompound(yc))
    t2 = datetime.now()
    print(f'time to add candidates: {t2 - t1}')

    pickle.dump(tuple(ycs), open(f'dumps/unfuge_candidates_added/{year}ycs', 'wb'))
