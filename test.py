# from ttrcontainer import TTRContainer
# from nltk import word_tokenize
# import sys
# import os

# import spacy

# path_to_corpora = 'corpora/'
# candidates_file = 'SECOS/data/denews70M_trigram__candidates'

# def generate_paths(prefix, suffix):
#     filename_list = []
#     for year in range(1995, 2023):
#         identifier = prefix + str(year) + '_1M'
#         filename_list.append(path_to_corpora + identifier + '/' + identifier + suffix)
#     return filename_list

# wordsfile_paths = generate_paths('deu_news_', '-words.txt')
# sentencesfile_paths = generate_paths('deu_news_', '-sentences.txt')

# _________________________________________________________


# def is_compound(word):
#     #no idea how to determine this at the moment
#     word_is_compound = False #haha
#     if (word_is_compound):
#         return True
#     else:
#         return False

# # for testing :)
# sentences_1995 = open(sentencesfile_paths[0]).readlines()
# for i, sentence in enumerate(sentences_1995):
#     j = sentence.find('\t')
#     sentences_1995[i] = sentence[j+1:]

# nlp = spacy.load('de_core_news_sm')

# sentence = sentences_1995[2]

# print(sentence)

# doc = nlp(sentence)

# for token in doc:
#     print(token.text + ' ' + str(token.tag_) + '\n')

# text = open(sentencesfile_paths[0]).read()
# if len(text) < nlp.max_length:
#     nlp.max_length = len(text) + 1

# def clear():
#     """clear stdout (unix)"""
#     os.system( 'clear' )

# def make_ttr_container(path):
#     f = open(path)
#     tokenized = []
#     for index, line in enumerate(f.readlines()):
#         print(index)
#         for token in word_tokenize(line):
#             tokenized.append(token)
#     return TTRContainer(tokenized)

# container_1995 = make_ttr_container(sentencesfile_paths[0])

# _________________________________________________________

# from yeared_compound import YearedCompound
# import pickle

# ycs = []
# wordfile = open('corpora/deu_news_1995_1M/deu_news_1995_1M-words.txt')

# for line in wordfile.readlines()[20000:20050]:
#     split = line.split()
#     words = split[1:-1]
#     word = ' '.join(words)
#     yc = YearedCompound(word,'1995',split[-1],'PDW','news')
#     if yc.is_compound:
#         ycs.append(yc)

# for yc in ycs:
#     print(str(yc) + '\n')

# _________________________________________________________

# import pickle
# ycs = pickle.load(open('dumps/1995ycs', 'rb'))

# from flair.nn import Classifier
# from flair.data import Sentence as FlairSentence

# tagger = Classifier.load('flair/ner-multi-fast')

# for yc in ycs[100000:100050]:
#     token = FlairSentence(yc.text)
#     tagger.predict(token)
#     print(str(token) + '\n')

# token1 = FlairSentence(ycs[20].text)
# token2 = FlairSentence(ycs[100000].text)
# tagger.predict(token1)
# tagger.predict(token2)
# print(str(token1.get_labels()) + '\n')
# print(str(token2.get_labels()))

# _________________________________________________________

# import pickle
# ycs = pickle.load(open('dumps/1995ycs', 'rb'))

# from flair.nn import Classifier
# from flair.data import Sentence as FlairSentence

# tagger = Classifier.load('flair/ner-multi-fast')

# import datetime

# predictions = []

# def is_not_name(yc):
#     token = FlairSentence(yc.text)
#     tagger.predict(token)
#     return len(token.labels) > 0

# filtered = filter(is_not_name, ycs)

# # benchmark for proof
# prevtime = datetime.datetime.now()
# for f in filtered:
#     time = datetime.datetime.now()
#     elapsed = time - prevtime
#     prevtime = time
#     print(elapsed)

# outfile = open('dumps/1995ycs_ner_filtered', 'wb')
# pickle.dump(list(filtered), outfile)


# _________________________________________________________

# import pickle
# import spacy

# # ycs = pickle.load(open('dumps/2000ycs', 'rb'))

# # for i in range(100000, 200000)[::500]:
# #     print('\t\t'.join((ycs[i].text, ycs[i].splits[0])))

# words_to_try = ['Bundes',
#                 'Aushilfs',
#                 'Bevolkerungs',
#                 'Bühnen',
#                 'Bildungs',
#                 'Boxen',
#                 'Buchen',
#                 'Cervantes',
#                 'Ausschuss',
#                 'Abwasser',
#                 'verdienen',
#                 'systemen',
#                 'hochburg',
#                 'Wachtums',
#                 'Zinssignale',
#                 'Zins',
#                 'Devisen',
#                 'Howaldts',
#                 'machst',
#                 'trockener',
#                 'trocken',
#                 'trockens']

# nlp = spacy.load('de_core_news_md')

# for word in words_to_try:
#     doc = nlp(word)
#     for token in doc:
#         print(word + ' ' + str(token.lemma_))

# _________________________________________________________

# from unfuge import operations
# import dill as pickle
# from tabulate import tabulate

# ycs = pickle.load(open('dumps/numbers_filtered/2000ycs', 'rb'))

# subset = ycs[::20000]

# heads_only = []
# heads_only_lemmatized = []

# for yc in subset:
#     for split in yc.splits[:-1]:
#         heads_only.append(split)
#     for lemma in yc.lemmas[:-1]:
#         heads_only_lemmatized.append(lemma)

# def extract(s, s_lemmatized):
#     l = []
#     l_lemmatized = []
#     table = [operations.keys()]
#     for key, value in operations.items():
#         l.append(value(s))
#         l_lemmatized.append(value(s_lemmatized))
#     table.append(l)
#     table.append(l_lemmatized)
#     return table

# for i in range(len(heads_only)):
#     table = extract(heads_only[i], heads_only_lemmatized[i])
#     print(tabulate(table))

# _________________________________________________________

# from unfuge import operations

# s = 'bobb'
# b = 'bill'

# print(operations['DEL_E'](b))
# print(operations['DEL_E'](s))

# a = 'happen'
# c = 'enstance'

# print(operations['ADD_EN'](a))
# print(operations['ADD_EN'](c))

# _________________________________________________________

# import dill as pickle
# from datetime import datetime
# import os

# print(f'pid: {os.getpid()}')

# def load_year(year):
#     t1 = datetime.now()
#     ycs = pickle.load(open(f'dumps/unfuge_candidates_added/{year}ycs', 'rb'))
#     t2 = datetime.now()
#     elapsed = t2 - t1
#     print(f'time to load {year}: {elapsed}')
#     return ycs

# years = {}

# for year in range(1995, 2000):
#     print(f'counting year: {year}')
#     years[year] = {}
#     ycs = load_year(year)

#     for yc in ycs:
#         matches = yc.lemma_matches
#         for match in matches:
#             for key in match.keys():
#                 if key not in years[year].keys():
#                     years[year][key] = 0
#                 years[year][key] += 1

# for year, matchdict in years.items():
#     print(f'results for year: {year}')
#     for key, count in matchdict.items():
#         print(f'{key}: {count}')
#     print('\n')

# _________________________________________________________

# import requests

# request_prefix = "http://localhost:2020?sentence="

# class YearedCompound:
#     """
#     Stores relevant data for a compound from the corpus inc:
#     year, number of occurances, corpus, type of corpus (eg news, website, ...?),
#     splits, Fugenelement(e?)
#     """
#     def __init__(self, text, year, count, corpus, source) -> None:
#         # CHOP IT UP
#         response = requests.get(request_prefix + text)
#         response.encoding = 'UTF-8'
#         self.splits = response.text.split()
#         if len(self.splits) < 2:
#             self.is_compound = False
#             return
#         else:
#             self.is_compound = True

#         self.text = text
#         self.year = year
#         self.count = count
#         self.corpus = corpus
#         self.source = source

#         pass # we will do determination of fugenelemente right here

#     def __str__(self):
#         return '\n'.join([
#             'word:\t\t' + self.text,
#             'year:\t\t' + str(self.year),
#             'count:\t\t' + str(self.count),
#             'corpus:\t\t' + self.corpus,
#             'source:\t\t' + self.source,
#             'splits:\t\t' + ' '.join(self.splits)
#         ])


# _________________________________________________________

import dill as pickle
import re

matcher = re.compile(r'.*[aeiouöüä]+r?ch$')

nah_words = {'fach', 'durch', 'bruch', 'nach', 'rauch', 'gleich', 'hoch', 'buch', 'stich', 'reich', 'sprech', 'lich', 'flach', 'schlauch', 'hauch', 'schwach', 'wach', 'hauch', 'dach'}
def no_nahs(s):
    for w in nah_words:
        if s[-len(w):].lower() == w:
            return False
    return True

for year in range(1995, 2023):
    ycs = pickle.load(open(f'dumps/named_ents_filtered/{year}ycs', 'rb'))

    for text, yc in ycs.items():
        s = yc.splits[0].lower()

        if no_nahs(s) and matcher.match(s):
            pass
