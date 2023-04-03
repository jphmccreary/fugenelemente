import dill as pickle

ycs = pickle.load(open('dumps/unfuge_candidates_added/2022ycs', 'rb'))

# for yc in ycs[20000:30000:1000]:
#     print(f'{yc.text} {yc.count}')

for yc in ycs:
    if yc.text == 'Studienjahr':
        print(f'{yc.fuge_candidates}\n{yc.lemma_matches}')
        break
