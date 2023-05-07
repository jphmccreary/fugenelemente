import dill as pickle
from datetime import datetime
from constants import PREPOSITIONS
from collections import defaultdict
import re

caps_matcher = re.compile(r'[A-ZÄÖÜ]')
lemma_map = {}
lemmas = set()
lemma_file = open('lemmatization-de.txt')
for line in lemma_file.readlines():
    [lemma, token] = line.split()
    lemma_map[token] = lemma
    lemmas.add(lemma)

def pick_lemma_from_pair(matches):
    [a, b] = matches
    if a in lemma_map and lemma_map[a] == b:
        return b
    if b in lemma_map and lemma_map[b] == a:
        return a
    else:
        return min(matches, key=len)

# generalizes the above
# bad. bad. just returns the first match that is the lemma of another match
# probably will usually just return the shortest?
# could be more than one. no time to fix.
# ideally i'd use some kind of semantic analysis to sort candidates
def pick_lemma_from_many(matches):
    for match in matches:
        without_that_one = list(matches)
        without_that_one.remove(match)
        if match in lemma_map and lemma_map[match] in without_that_one:
            return lemma_map[match]
    shortest = min(matches, key=len)
    return shortest

def old_lemma_fn(yc):
    for fn, candidate in yc.fuge_candidates[0].items():
        if candidate == yc.old_lemmas[0]:
            return fn, True
    return 'NULL', False

t0 = datetime.now()
for year in range(1995, 2023):
    t1 = datetime.now()
    elapsed = t1 - t0
    t0 = t1
    print(f'{year}\t{elapsed}')
    ycs = pickle.load(open(f'dumps/named_ents_filtered/{year}ycs', 'rb'))
    countsfile = open(f'corpora/deu_news_{year}_1M/deu_news_{year}_1M-words.txt')
    counts = defaultdict(int)
    for line in countsfile.readlines():
        if len(line.split()) != 3:
            continue
        _, word, count = line.split()
        counts[word] = int(count)
    # messy af, out of time
    for text, yc in ycs.items():
        matches = []
        for fn, candidate in yc.fuge_candidates[0].items():
            if candidate in lemmas:
                matches.append(candidate)
        if len(matches) == 0:
            fn, found = old_lemma_fn(yc)
            if found:
                yc.lemma_found = True
                lemma = yc.fuge_candidates[0][fn]
            elif yc.splits[0].lower() not in PREPOSITIONS:
            #     dictionary lookup
                yc.lemma_found = False
                for fn, candidate in yc.fuge_candidates[0].items():
                    if candidate in lemma_map:
                        matches.append(candidate)
            else:
                yc.lemma_found = False
        elif len(matches) == 2:
            yc.lemma_found = True
            lemma = pick_lemma_from_pair(matches)
        elif len(matches) > 2:
            yc.lemma_found = True
            lemma = pick_lemma_from_many(matches)
        else:
            yc.lemma_found = True
            lemma = matches[0]

        if yc.lemma_found:
            candidates = yc.fuge_candidates[0].items()
            for fn, defuged in candidates:
                if lemma == defuged:
                    yc.chosen_fn = fn
                    break #?
        # pick best dictionary match
        elif len(matches) > 0:
            yc.chosen_fn = 'NULL'
            chosen_word = max(matches, key=lambda x: counts[x])
            candidates = yc.fuge_candidates[0].items()
            for fn, defuged in candidates:
                if chosen_word == defuged:
                    yc.chosen_fn = fn
                    if caps_matcher.match(yc.text[0]):
                        pass
                    break #?
        else:
            yc.chosen_fn = 'NULL'
    with open(f'dumps/lemma_lookup_trial/{year}ycs', 'wb') as out_file:
        pickle.dump(ycs, out_file)




# print(f'single matches: {single_match}')
# print(f'no matches: {no_match}')
# print(f'multi matches: {multi_match}')
