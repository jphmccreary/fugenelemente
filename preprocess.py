import re

path_to_corpora = 'corpora/'
candidates_file = 'SECOS/data/denews70M_trigram__candidates'

#? will this be sufficient? should foreign characters be considered?
german_regex = re.compile('[a-zA-ZäÄöÖüÜß-]+')

def generate_paths_w_file(prefix, suffix):
    filename_list = []
    for year in range(1995, 2023):
        identifier = prefix + str(year) + '_1M'
        filename_list.append(path_to_corpora + identifier + '/' + identifier + suffix)
    return filename_list

def generate_directory_list(prefix):
    directory_list = []
    for year in range(1995, 2023):
        identifier = prefix + str(year) + '_1M'
        directory_list.append(path_to_corpora + identifier + '/')
    return directory_list

wordsfile_paths = generate_paths_w_file('deu_news_', '-words.txt')
# sentencesfile_paths = generate_paths('deu_news_', '-sentences.txt')
directories = generate_directory_list('deu_news_')

def generate_word_list(wordsfile_path):
    f = open(wordsfile_path)
    word_list = []
    for line in f.readlines():
        word = line.split()[1]
        if german_regex.match(word):
            word_list.append(word)
    return word_list

for i, wordsfile_path in enumerate(wordsfile_paths):
    directory = directories[i]
    outfile = open(directory + 'words_only.txt', 'w')
    wordlist = generate_word_list(wordsfile_path)
    outfile.write('\n'.join(wordlist))

