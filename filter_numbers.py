import dill as pickle
import re

number_regex = re.compile('[0-9]')

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

def has_no_numbers(yc):
    return not number_regex.search(yc.text)

for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/lemmatized/{year}ycs', 'rb'))
    filtered = filter(has_no_numbers, ycs)
    outfile = open(f'dumps/numbers_filtered/{year}ycs', 'wb')
    pickle.dump(tuple(filtered), outfile)

