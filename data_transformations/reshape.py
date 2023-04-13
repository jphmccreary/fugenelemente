import dill as pickle
from yeared_compound import YearedCompound
from datetime import datetime

for year in range(1996, 2023):

    print(f'loading year: {year}')
    t0 = datetime.now()
    ycs = pickle.load(open(f'dumps/unfuge_candidates_added/{year}ycs', 'rb'))
    t1 = datetime.now()
    print(f'time to load: {t1 - t0}')

    print('reshaping...')
    t0 = datetime.now()
    reshaped = {}
    for yc in ycs:
        reshaped[yc.text] = YearedCompound(
            corpus=0,
            count=int(yc.count),
            fuge_candidates=yc.fuge_candidates,
            old_lemmas=yc.lemmas,
            source=0,
            splits=tuple(yc.splits),
            text=yc.text,
            year=year
        )
    t1 = datetime.now()
    print(f'time to reshape: {t1 - t0}')

    print('dumping...')
    t0 = datetime.now()
    outfile = open(f'dumps/reshaped/{year}ycs', 'wb')
    pickle.dump(reshaped, outfile)
    t1 = datetime.now()
    print(f'time to dump: {t1 - t0}\n')


