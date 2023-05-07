import dill as pickle

ent_tags = {'PER', 'LOC', 'ORG', 'MISC'}
def is_named_ent(yc):
    yes_ct = 0
    no_ct = 0
    for tag, count in yc.ent_types.items():
        if tag in ent_tags:
            yes_ct += count
        else:
            no_ct += count
    if yes_ct >= no_ct:
        return True
    return False

for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/invalid_chars_filtered/{year}ycs', 'rb'))
    kept = {}
    for text, yc in ycs.items():
        if not is_named_ent(yc):
            kept[text] = yc
    with open(f'dumps/named_ents_filtered/{year}ycs', 'wb') as outfile:
        pickle.dump(kept, outfile)
