from search import search
from bs4 import BeautifulSoup
import urllib2
import config

artists = config.artists
outputfilename = "lyrics.csv"
client_access_token = "your-access-token"

def get_lyrics(url):
    request = urllib2.Request(url)
    request.add_header("Authorization", "Bearer " + client_access_token)
    request.add_header("User-Agent",
                       "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")  # Must include user agent of some sort, otherwise 403 returned

    page = urllib2.urlopen(request)
    soup = BeautifulSoup(page, "lxml")
    lyrics = soup.find("div", class_= "lyrics")
    return lyrics.text

f2 = open('urls', 'wb')

for artist in ["Eminem"]:
    a = search(artist, outputfilename, client_access_token)
    urls = map(lambda t: t[3], a)
    print artist, len(urls)

    f = open('lyrics/' + artist, 'wb')
    f2.write(artist)
    for url in urls:
        lyrics = get_lyrics(url)
        f2.write(url)
        print url
        f.write(lyrics.encode("utf8"))

    f.close()
f2.close()