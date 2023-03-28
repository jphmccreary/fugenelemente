import dill as pickle
from datetime import datetime
import os

print(f'pid: {os.getpid()}')

def load_year(year):
    t1 = datetime.now()
    ycs = pickle.load(open(f'dumps/unfuge_candidates_added/{year}ycs', 'rb'))
    t2 = datetime.now()
    elapsed = t2 - t1
    print(f'time to load {year}: {elapsed}')
    return ycs

years = {}

for year in range(1995, 2000):
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

for year, matchdict in years.items():
    print(f'results for year: {year}')
    for key, count in matchdict.items():
        print(f'{key}: {count}')
    print('\n')
