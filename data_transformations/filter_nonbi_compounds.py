import dill as pickle

for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/reshaped/{year}ycs', 'rb'))
    filtered = {}
    for key, yc in ycs.items():
        if len(yc.splits) == 2:
            filtered[key] = yc
    print(f'dumping year: {year}...')
    pickle.dump(filtered, open(f'dumps/nonbi_filtered/{year}ycs', 'wb'))
