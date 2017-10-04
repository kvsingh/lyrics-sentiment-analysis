import re
import os, config

artists = config.artists

for artist in artists:
    f = open('lyrics/' + artist, 'rb')
    all_words = ''
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        all_words += this_sentence

    f.close()

    #remove identifiers like chorus, verse, etc
    all_words = re.sub(r'[\(\[].*?[\)\]]', '', all_words)

    all_words = os.linesep.join([s for s in all_words.splitlines() if s])
    print all_words

    f = open('lyrics/' + artist + '-cleaned', 'wb')
    f.write(all_words.encode('utf-8'))
    f.close()
