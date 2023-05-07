import dill as pickle

ycs0 = pickle.load(open('dumps/lemma_lookup_trial/1995ycs', 'rb'))
ycs1 = pickle.load(open('dumps/lemma_lookup_trial/2022ycs', 'rb'))

count0 = 0
count1 = 0

types0 = {}
types1 = {}
changes = []

for text, yc in ycs0.items():
    count0 += yc.count
    if yc.chosen_fn == 'DEL_E_ADD_I':
        types0[text] = yc.count

for text, yc in ycs1.items():
    count1 += yc.count
    if yc.chosen_fn == 'DEL_E_ADD_I':
        types1[text] = yc.count

for t in types0:
    if t not in types1:
        types1[t] = 0

for t in types1:
    if t not in types0:
        types0[t] = 0

all_types = set.union(set(types0.keys()), set(types1.keys()))

for t in all_types:
    changes.append((t, types1[t] - types0[t]))

sorted_changes = sorted(changes, key=lambda x: x[1], reverse=False)

print(sorted_changes[:50])
