import dill as pickle
from constants import INVALID_CHARS

for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/named_ents_marked/{year}ycs', 'rb'))
    kept = {}
    for text, yc in ycs.items():
        invalid_found = False
        for char in text:
            if char in INVALID_CHARS:
                invalid_found = True
                break
        if not invalid_found:
            # secret extra step to remove ycs that spacy didn't tokenize the same way
            # and to remove failed pos tagging and whole lemmatization by spacy
            if hasattr(yc, 'ent_types'):
                delattr(yc, 'tags')
                delattr(yc, 'whole_lemmas')
                kept[text] = yc
    with open(f'dumps/invalid_chars_filtered/{year}ycs', 'wb') as outfile:
        pickle.dump(kept, outfile)
