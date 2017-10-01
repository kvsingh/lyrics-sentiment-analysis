import nltk
#from __future__ import division
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  # Filter out stopwords, such as 'the', 'or', 'and'
import pandas as pd
import config
import matplotlib.pyplot as plt

artists = config.artists
df = pd.DataFrame(columns=('artist', 'words'))

i=0
for artist in artists:
    f = open('lyrics/' + artist + '-cleaned', 'rb')
    all_words = ''
    num_words = 0
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        num_words_this = len(this_sentence.split(" "))
        all_words += this_sentence
        num_words += num_words_this
        #print num_words_this

    df.loc[i] = (artist, num_words)
    print artist, num_words
    i+=1

df.plot.bar(x='artist', y='words', title='Number of Words for each Artist');
plt.show()