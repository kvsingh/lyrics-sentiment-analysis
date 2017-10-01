from textblob import TextBlob
import config
artists = config.artists

sentiments = []

for artist in artists:
    f = open('lyrics/' + artist + '-cleaned', 'rb')
    all_words = ''
    avg = 0
    num = 0
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        all_words += this_sentence
        blob = TextBlob(this_sentence)
        avg += blob.polarity
        num+=1

    avg = avg / num

    blob = TextBlob(all_words)
    #print artist, avg, blob.polarity
    sentiments.append((artist, avg, blob.polarity))

print sorted(sentiments, key=lambda a:a[1], reverse=True)
