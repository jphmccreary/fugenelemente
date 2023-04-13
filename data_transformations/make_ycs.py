from yeared_compound import YearedCompound
import pickle
import datetime
import os

print('pid: ' + str(os.getpid()))

for year in range(1995, 2023):
    starttime = datetime.datetime.now()
    print('beginning ' + str(year) + ' at time: ' + str(starttime))

    ycs = []
    wordfile = open('corpora/deu_news_' + str(year) + '_1M/deu_news_' + str(year) + '_1M-words.txt')

    for line in wordfile.readlines():
        split = line.split()
        words = split[1:-1]
        word = ' '.join(words)
        yc = YearedCompound(word, str(year), split[-1], 'PDW', 'news')
        if yc.is_compound:
            ycs.append(yc)

    outfile = open('dumps/' + str(year) + 'ycs', 'wb')

    pickle.dump(ycs, outfile)
    outfile.close()

    finishtime = datetime.datetime.now()
    print('finish time: ' + str(finishtime))
    print('elapsed: ' + str(finishtime - starttime) + '\n')
