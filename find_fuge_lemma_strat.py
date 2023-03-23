import spacy
import pickle
import datetime

# (Länger 1998)
FUGENELEMENTE = {
    'NULL': '',
    'ADD_S': 's',
    'ADD_N': 'n',
    'ADD_EN': 'en',
    'ADD_NEN': 'nen',
    'DEL_US_ADD_EN': 'en',
    'DEL_UM_ADD_EN': 'en',
    'DEL_UM_ADD_A': 'a',
    'DEL_E': '',
    'DEL_A_ADD_EN': 'en',
    'ADD_E': 'e',
    'UMLAUT_ADD_E': 'e',
    'DEL_ON_ADD_EN': 'en',
    'ADD_ES': 'es',
    'UMLAUT_ADD_ER': 'er',
    'DEL_EN': '',
    'DEL_ON_ADD_A': 'a',
    'ADD_ER': 'er',
    'ADD_IEN': 'ien',
    'DEL_E_ADD_I': 'i',
}

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
