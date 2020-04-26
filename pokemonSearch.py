import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

pokes = open("pokefinal.txt","r")
pokesText = pokes.read()
pokeList = []
for line in pokesText.split():
    pokeList.append(line)

def getPoke(img_link):
    filePath = img_link
    searchUrl = 'http://www.google.com/searchbyimage?image_url='
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    url = searchUrl + filePath
    r = requests.get(url, headers=headers, allow_redirects= True)
    soup = BeautifulSoup(r.content, "html.parser")
    text = (''.join(s.findAll(text=True))for s in soup.findAll('div'))

    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    log = open("log.txt", "a", encoding="utf-8")
    log.write(url)
    log.write("\n")
    ind = 1
    for i in c.most_common():
        if ind == 99:
            ind += 1
            log.write(str(i))
        elif ind < 100:
            ind += 1
            log.write(str(i) + ",")
        else:
            break
    log.write("\n\n")
    log.close()
    for x in c.most_common():
        if x[0] in pokeList:
            result = x[0]
            return (result)
