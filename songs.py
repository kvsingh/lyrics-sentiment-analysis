from search import search
from bs4 import BeautifulSoup
import urllib2
import config

artists = config.artists
outputfilename = "lyrics.csv"
client_access_token = "ugjWi8MlOxPQkOL-q0WUFpwaN2nZg76bv8cuHl6mjXPi4wvxE3TcNxdWjE1zbVPr"

def get_lyrics(url):
    request = urllib2.Request(url)
    request.add_header("Authorization", "Bearer " + client_access_token)
    request.add_header("User-Agent",
                       "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")  # Must include user agent of some sort, otherwise 403 returned

    page = urllib2.urlopen(request)
    print url
    soup = BeautifulSoup(page, "lxml")
    lyrics = soup.find("div", class_= "lyrics")
    return lyrics.text

for artist in artists:
    a = search(artist, outputfilename, client_access_token)
    urls = map(lambda t: t[3], a)
    print artist, len(urls)

    f = open('lyrics/' + artist, 'wb')
    for url in urls:
        lyrics = get_lyrics(url)
        #print lyrics
        f.write(lyrics.encode("utf8"))

    f.close()