import dill as pickle
from datetime import datetime
import os

print(f'pid: {os.getpid()}')

# (Länger, 1998)
# out of 46700 total
# these are also the keys for the dicts that reference them
FUGENELEMENTE_FREQUENCY_ORDER = (
    'NULL',             # 48.7%
    'ADD_S',            # 20.6%
    'ADD_N',            # 11.4%
    'ADD_EN',           # 9.2%
    'ADD_NEN',          # 5.6%
    'DEL_US_ADD_EN',    # 1.3%
    'DEL_UM_ADD_EN',    # 0.7%
    'DEL_UM_ADD_A',
    'DEL_E',
    'DEL_A_ADD_EN',
    'ADD_E',
    'UMLAUT_ADD_E',
    'DEL_ON_ADD_EN',
    'ADD_ES',
    'UMLAUT_ADD_ER',
    'DEL_EN',
    'DEL_ON_ADD_A',
    'ADD_ER',
    'ADD_IEN',
    'DEL_E_ADD_I',
)

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
table = [['']]
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
