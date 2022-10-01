import random
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

#A single function, getLinks, that takes in a Wikipedia article URL of the form
#/wiki/<Article_Name> and returns a list of all linked article URLs in the same form.
#build a scraper that collects the title, the first para‐ graph of content,
arcLinksSet = set() #so i wouldnt visit the same article link again


def getWikiLinks(url):
    global arcLinksSet
    try:
        html = urlopen('https://en.wikipedia.org{}'.format(url))
        bs = BeautifulSoup(html, "html.parser")
        links = bs.find('div', {'id': "bodyContent"}).find_all('a', 
        {'href': re.compile('^(/wiki/)((?!:).)*$')})
        #title is in span class="mw-page-title-main"
        print(bs.h1.get_text())
        # print(titleList)
        #fist para is first p of div class="mw-parser-output"
        print(bs.find('div', {'class':"mw-parser-output"}).find('p'))
        # print(paragraphList)
    except HTTPError or URLError or AttributeError:
        print("something is missing")
        return None
    else:
        for link in links:
            if("href" in link.attrs):
                #print(link['href']) -> prints all internal links
                arcLinksSet.add(link['href'])

#A main function that calls getLinks with a starting article,
#chooses a random article link from the returned list, and calls getLinks again, 
#until you stop the program or until no article links are found on the new page.
i = 0
def main(url):
    print(url)
    global i
    getWikiLinks(url)
    url = random.choice(tuple(arcLinksSet))
    print('-'*20, "\n")
    i+=1
    if(i==5):
        return 
    main(url) #recursion is recommended for small sites only


url = '/wiki/Kevin_Bacon'
main(url)



    
    



