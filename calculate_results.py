import dill as pickle
from constants import FUGENELEMENTE_FREQUENCY_ORDER
from collections import defaultdict
from yeared_compound import YearedCompound
import re
import math

caps_matcher = re.compile(r'[A-ZÄÖÜ]')
capsed_only = True
max_count = math.inf
# fill out a dict with years
years = {}
for year in range(1995, 2023):
    years[year] = defaultdict(int)
    for fn in FUGENELEMENTE_FREQUENCY_ORDER:
        years[year][fn]

# store the ycs that have more than one match to an old_lemma (or none at all, don't think that's possible though)
no_match = []
multi_match = []

dump_folder = 'lemma_lookup_trial'
for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/{dump_folder}/{year}ycs', 'rb'))
    for text, yc in ycs.items():
        if yc.count > max_count:
            continue
        if capsed_only and not re.match(caps_matcher, text):
            continue
        years[year][yc.chosen_fn] += yc.count

# top row
results = [['Year']]
for fn in FUGENELEMENTE_FREQUENCY_ORDER:
    results[0].append(fn)

for year in years:
    total = sum(years[year].values())
    results.append([str(year)])
    for fn in FUGENELEMENTE_FREQUENCY_ORDER:
        results[-1].append(str(years[year][fn] / total))

csv_string = ''
for line in results:
    csv_string += ','.join(line) + '\n'

with open('results/test.csv', 'w') as outfile:
    outfile.write(csv_string)

with open('dumps/results', 'wb') as outfile:
    pickle.dump(results, outfile)
