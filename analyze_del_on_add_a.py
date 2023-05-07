import dill as pickle

types95 = {}
types22 = {}
ycs95 = pickle.load(open('dumps/lemma_lookup_trial/1995ycs', 'rb'))
ycs22 = pickle.load(open('dumps/lemma_lookup_trial/2022ycs', 'rb'))

count95 = 0
count22 = 0

for text, yc in ycs95.items():
    count95 += yc.count
    if yc.chosen_fn == 'DEL_ON_ADD_A':
        types95[text] = yc.count

for text, yc in ycs22.items():
    count22 += yc.count
    if yc.chosen_fn == 'DEL_ON_ADD_A':
        types22[text] = yc.count

for t in types95:
    if t not in types22:
        types22[t] = 0

for t in types22:
    if t not in types95:
        types95[t] = 0

all_types = set.union(set(types95.keys()), set(types22.keys()))
all_sorted = sorted(list(all_types))

interesting = set()

# medien_count = 0
# for t in all_types:
#     if t.startswith('Medien'):
#         medien_count += types95[t] + types22[t]
#     elif not t.startswith('Daten'):
#         interesting.add(t)

# daten_count95 = 0
# daten_count22 = 0
# for t in all_types:
#     if t.startswith('Daten'):
#         daten_count95 += types95[t]
#         daten_count22 += types22[t]

csv_string = 'word,1995 count,2022 count,1995 proportion,2022 proportion\n'
for t in all_types:
    csv_string += f'{t},{types95[t]},{types22[t]},{types95[t]/count95},{types22[t]/count22}\n'

with open('results/del_on_add_a.csv', 'w') as outfile:
    outfile.write(csv_string)

print(interesting)
pass
