import dill as pickle

for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/nonbi_filtered/{year}ycs', 'rb'))
    filtered = {}
    for key, yc in ycs.items():
        if yc.count > 1:
            filtered[key] = yc
    print(f'dumping year: {year}...')
    pickle.dump(filtered, open(f'dumps/no_cooc_filtered/{year}ycs', 'wb'))
