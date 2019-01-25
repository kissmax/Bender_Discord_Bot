import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
pokes = open("C:/Users/Max Kiss/Desktop/Bender/pokefinal.txt","r")
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
    print (url)
    r = requests.get(url, headers=headers, allow_redirects= True)
    soup = BeautifulSoup(r.content, "html.parser")
    text = (''.join(s.findAll(text=True))for s in soup.findAll('div'))

    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))

    for x in c.most_common():
        print (x)
        if x[0] in pokeList:
            result = x[0]
            return (result)
    """for i in range(0,5):
        if (common[i][0] not in ['',' ','pokemon','Pokémon','pokémon','is','the','and','sun','go','moon','evolution','a','to','in','wiki', 'of', 'x','×']):
            result += common[i][0] + " "
    words = result.split()"""

