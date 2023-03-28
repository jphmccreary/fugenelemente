import pickle
import spacy

# ycs = pickle.load(open('dumps/2000ycs', 'rb'))

# for i in range(100000, 200000)[::500]:
#     print('\t\t'.join((ycs[i].text, ycs[i].splits[0])))

words_to_try = ['Bundes',
                'Aushilfs',
                'Bevolkerungs',
                'Bühnen',
                'Bildungs',
                'Boxen',
                'Buchen',
                'Cervantes',
                'Ausschuss',
                'Abwasser',
                'verdienen',
                'systemen',
                'hochburg',
                'Wachtums',
                'Zinssignale',
                'Zins',
                'Devisen',
                'Howaldts',
                'machst',
                'trockener',
                'trocken',
                'trockens']

nlp = spacy.load('de_core_news_md')

for word in words_to_try:
    doc = nlp(word)
    for token in doc:
        print(word + ' ' + str(token.lemma_))
