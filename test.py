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

import pickle
ycs = pickle.load(open('dumps/1995ycs', 'rb'))

from flair.nn import Classifier
from flair.data import Sentence as FlairSentence

tagger = Classifier.load('flair/ner-multi-fast')

import datetime

predictions = []

def is_not_name(yc):
    token = FlairSentence(yc.text)
    tagger.predict(token)
    return len(token.labels) > 0

filtered = filter(is_not_name, ycs)

# benchmark for proof
prevtime = datetime.datetime.now()
for f in filtered:
    time = datetime.datetime.now()
    elapsed = time - prevtime
    prevtime = time
    print(elapsed)

outfile = open('dumps/1995ycs_ner_filtered', 'wb')
pickle.dump(list(filtered), outfile)
