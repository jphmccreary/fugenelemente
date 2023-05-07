import dill as pickle
from datetime import datetime
import os
from constants import FUGENELEMENTE_FREQUENCY_ORDER

print(f'pid: {os.getpid()}')

def load_year(year):
    t1 = datetime.now()
    ycs = pickle.load(open(f'dumps/unfuge_candidates_added/{year}ycs', 'rb'))
    t2 = datetime.now()
    print(f'time to load {year}: {t2 - t1}')
    return ycs

years = {}

for year in range(1995, 2023):
    print(f'counting year: {year}')
    years[year] = {}
    ycs = load_year(year)

    for yc in ycs:
        matches = yc.lemma_matches
        for match in matches:
            for key in match.keys():
                if key not in years[year].keys():
                    years[year][key] = 0
                years[year][key] += 1

# for year, matchdict in years.items():
#     print(f'results for year: {year}')
#     for key, count in matchdict.items():
#         print(f'{key}: {count}')
#     print('\n')

# add the top row
table = [['year']]
for op in FUGENELEMENTE_FREQUENCY_ORDER:
    table[0].append(op)

for year, matchdict in years.items():
    entry = [year]
    for op in FUGENELEMENTE_FREQUENCY_ORDER:
        if op not in matchdict.keys():
            entry.append(0)
        else:
            entry.append(matchdict[op])
    table.append(entry)

csv_string = ''
for entry in table:
    csv_string += ','.join(str(s) for s in entry) + '\n'

outfile = open('lemma_strat_counts.csv', 'w')
outfile.write(csv_string)
