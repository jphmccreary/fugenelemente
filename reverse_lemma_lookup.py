import json
import dill as pickle

lemmas = set()

for token, lemma in lookups.items():
    lemmas.add(lemma)

pickle.dump(lemmas, open('lemma_list', 'wb'))

print(len(lemmas))
