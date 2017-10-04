import nltk
from nltk.corpus import stopwords  # Filter out stopwords, such as 'the', 'or', 'and'
import pandas as pd
import config
import matplotlib.pyplot as plt

artists = config.artists
df1 = pd.DataFrame(columns=('artist', 'words'))
df2 = pd.DataFrame(columns=('artist', 'lexicalrichness'))

i=0
for artist in artists:
    f = open('lyrics/' + artist + '-cleaned', 'rb')
    all_words = ''
    num_words = 0
    raw_text = ''
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        raw_text += this_sentence
        num_words_this = len(this_sentence.split(" "))
        num_words += num_words_this

    words = raw_text.split(" ")
    filtered_words = [word for word in words if
                      word not in stopwords.words('english') and len(word) > 1 and word not in ['na',
                                                                                                'la']]  # remove the stopwords

    df1.loc[i] = (artist, num_words)

    a = len(set(filtered_words))
    b = len(words)

    df2.loc[i] = (artist, (a / float(b)) * 100)
    i+=1

df1.plot.bar(x='artist', y='words', title='Number of Words for each Artist');
df2.plot.bar(x='artist', y='lexicalrichness', title='Lexical richness of each Artist');
#plt.show()