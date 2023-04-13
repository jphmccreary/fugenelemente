import dill as pickle

class YearedCompound:
    def __init__(self, source_yc):
        self.is_compound = source_yc.is_compound
        self.text = source_yc.text
        self.year = source_yc.year
        self.count = source_yc.count
        self.corpus = source_yc.corpus
        self.source = source_yc.source
        self.splits = tuple(source_yc.splits)

def has_no_spaces(yc):
    return ' ' not in yc.text

for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/{year}ycs', 'rb'))
    filtered = filter(has_no_spaces, ycs)
    outfile = open(f'dumps/spaces_filtered/{year}ycs', 'wb')
    pickle.dump(tuple(filtered), outfile)
