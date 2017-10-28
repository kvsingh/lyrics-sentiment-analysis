import re
import os, config
import string
from nltk import word_tokenize

artists = config.artists
translate_table = dict((ord(char), None) for char in string.punctuation)

for artist in ["radiohead"]:
    f = open('lyrics/' + artist + "-cleaned", 'rb')
    all_words = ''
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        all_words += this_sentence

    f.close()

    print all_words[:100]
    print "-------------"
    all_words = all_words.translate(translate_table)
    print all_words[:100]
    tokens = word_tokenize(all_words)
    print tokens