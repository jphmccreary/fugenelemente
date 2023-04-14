import dill as pickle
import string

translation = str.maketrans('', '', string.punctuation)

for year in range(1995, 2023):
    input_file = open(f'corpora/deu_news_{year}_1M/deu_news_{year}_1M-sentences.txt', 'r')
    ycs = pickle.load(open(f'dumps/no_cooc_filtered/{year}ycs', 'rb'))
    kept_sents = []
    count = 0
    print(f'filtering year: {year}')
    for line in input_file.readlines():
        tokens = map(lambda s: s.translate(translation), line.split())
        for token in tokens:
            if token in ycs:
                kept_sents.append(line)
                break

    input_file.close()

    with open(f'dumps/filtered_sents/{year}sents.txt', 'a') as output_file:
        for sent in kept_sents:
            output_file.write(f'{sent}')
