from wordcloud import WordCloud
import config

artists = config.artists

for artist in artists:
    f = open('lyrics/' + artist + '-cleaned', 'rb')
    all_words = ''
    avg = 0
    num = 0
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        all_words += this_sentence

    word_cloud = WordCloud(width=1000, height=500).generate(all_words)
    word_cloud.to_file('wordclouds/' + artist + ".png")
    image = word_cloud.to_image()

