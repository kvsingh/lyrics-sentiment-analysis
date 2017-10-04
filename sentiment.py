from nltk.sentiment.vader import SentimentIntensityAnalyzer

import config
artists = config.artists

df = pd.DataFrame(columns=('artist', 'pos', 'neu', 'neg'))
sid = SentimentIntensityAnalyzer()
i=0
for artist in artists:
    num_positive = 0
    num_negative = 0
    num_neutral = 0

    f = open('lyrics/' + artist + '-cleaned', 'rb')
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        comp = sid.polarity_scores(this_sentence)
        comp = comp['compound']
        if comp >= 0.5:
            num_positive += 1
        elif comp > -0.5 and comp < 0.5:
            num_neutral += 1
        else:
            num_negative += 1

    num_total = num_negative + num_neutral + num_positive
    percent_negative = (num_negative / float(num_total)) * 100
    percent_neutral = (num_neutral / float(num_total)) * 100
    percent_positive = (num_positive / float(num_total)) * 100
    df.loc[i] = (artist, percent_positive, percent_neutral, percent_negative)
    i+=1

df.plot.bar(x='artist', stacked=True)
plt.show()
