from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random


#Retrieves a list of all Internal links found on a page
def internalLinks(bs, includeUrl):
    try:
        includeUrl = "{}://{}".format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc) #gets the home page ex: http://youtube.com
        internalLinks = []
        #Finds all links that begin with a "/"
        for link in bs.find_all('a', {'href': re.compile('^(/|.*'+includeUrl+')$')}):
            if(link.attrs['href'] not in internalLinks
             and link.attrs['href'] is not None):
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    except HTTPError:
        print("error with finding page")
        return None
    except AttributeError:
        print("error with finding attributes")
        return None
    else:
        return internalLinks



#Retrieves a list of all external links found on a page
def externalLinks(bs, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" that do 
    #not contain the current URL
    try:
        for link in bs.find_all('a', {'href': re.compile('^(http(s)*|www)((?!'+
        excludeUrl+').)*$')}):
            if (link.attrs['href'] is not None 
            and link.attrs['href'] not in externalLinks):
                externalLinks.append(link.attrs['href'])
    except AttributeError:
        print("could find attribute")
        return
    else:
        return externalLinks


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, "html.parser")
    ExternalLinks = externalLinks(bs, urlparse(startingPage).netloc)
    if(len(ExternalLinks) == 0):
        print("no external links, looking around the site...")
        domain = '{}://{}'.format(urlparse(startingPage).scheme, 
        urlparse(startingPage).netloc)
        InternalLinks = internalLinks(bs, domain)
        if(len(InternalLinks) == 0):
            print("no internal or external links found!!")
            return
        else:
            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return ExternalLinks[random.randint(0, len(ExternalLinks)-1)]


i =0
def main(url):
    randomExternalLink = getRandomExternalLink(url)
    print("random external link is: ", randomExternalLink)
    global i
    i+=1
    if(i==5):
        return
    main(randomExternalLink)
    

main("https://en.wikipedia.org/")


        



    




