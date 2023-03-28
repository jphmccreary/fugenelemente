import spacy
import dill as pickle
import datetime
from unfuge import operations


# FUGENELEMENTE_grouped = {
#     '': ('NULL', 'DEL_E', 'DEL_EN'),
#     's': ('NULL', 'ADD_S', 'ADD_ES'),
#     'n': ('NULL', 'ADD_N'), # must ensure that it isn't en, nen, or ien
#     'en': ('NULL', 'ADD_N' 'ADD_EN', 'DEL_US_ADD_EN', 'DEL_UM_ADD_EN', 'DEL_ON_ADD_EN', 'DEL_A_ADD_EN')
# }

def load_stuff():
    nlp = spacy.load('de_core_news_md')
    ycs = pickle.load(open('dumps/1995ycs', 'rb'))
    return nlp, ycs

t1 = datetime.datetime.now()
nlp, ycs = load_stuff()
t2 = datetime.datetime.now()
elapsed = t2 - t1
print('time to load: ' + str(elapsed))

def find_fuge(splits: tuple) -> tuple:
    fugen = []
    return tuple(fugen)
