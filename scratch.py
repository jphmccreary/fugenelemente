import dill as pickle

ycs = pickle.load(open('dumps/reshaped/1995ycs', 'rb'))

pass

# shape = {
#     'corpus': str, # going to make these an int based on CORPUS_ID_MAP
#     'count': str, #? is it? it has apostrophes in the debugger. maybe should be an int
#     'fuge_candidates': tuple, # tuple(dict(str:str))
#     'is_compound': bool,
#     'lemma_matches': (dict), # tuple(dict(str:str))
#     'lemmas': (str), # tuple(str)
#     'source': str, # going to make these an int based on SOURCE_TYPE_MAP
#     'splits': [str], # list(str)
#     'text': str, #going to also make this the key for the dict that stores them,
#     'year': str,
# }
