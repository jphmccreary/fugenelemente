#!/usr/bin/env python3
import subprocess

# set arguments here (we will not be running different commands, just editing this file)
dt_candidates = 'SECOS/data/denews70M_trigram__candidates'
word_count_file = 'SECOS/data/denews70M_trigram__WordCount'
min_word_count = '50'
prefix_length = '3'
suffix_length = '3'
word_length = '5'
dash_word = '3'
upper = 'upper'
epsilon = '0.01'
port = '2020'

command = 'python2 SECOS/decompound_server.py ' + ' '.join([
    dt_candidates,
    word_count_file,
    min_word_count,
    prefix_length,
    suffix_length,
    word_length,
    dash_word,
    upper,
    epsilon,
    port
])

process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()  # receive output from the python2 script

print(output)
