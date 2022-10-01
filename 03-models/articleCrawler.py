from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


#simple general purpose crawler for articles

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print("URL: ", self.url)
        print("TITLE: ", self.title)
        print("BODY: ", self.body)

class Crawler:
    def getPage(self, url):
        try:
            html = urlopen(url)
            bs = BeautifulSoup(html, "html.parser")
        except HTTPError or URLError:
            print("encountered an error when downloading page content!!")
            return None
        else:
            return bs
    
    def getContent(self, bs, tag, attribute):
        content = bs.find(tag, attribute)
        if(content is not None):
            return content.get_text()
        else:
            print("content not found")
            return None

    def crawl(self, url, titleObj, bodyObj):
        #titleObj = [titleTag, attributes object of that tag]
        bs = self.getPage(url)
        title = self.getContent(bs, titleObj[0], titleObj[1])
        body = self.getContent(bs, bodyObj[0], bodyObj[1])
        content = Content(url, title, body)
        content.print()


crawler = Crawler()
titleObj = [
    ['h1', {'data-testid':"Heading"}],
    ['h1', {'class':"article__title"}]
]
bodyObj = [
    ['div',{'class':"article-body__content__17Yit paywall-article"}],
    ['div',{'class':"article-content"}]
]
urlObj = [
    "https://www.reuters.com/markets/commodities/coal-rush-energy-crisis-fires-global-hunt-polluting-fuel-2022-09-20/",
    "https://techcrunch.com/2022/09/20/revolut-cyberattack-thousands-exposed/"
]

#all i have to do is to point out where the title and body is on a certain website
#and the crawler does the rest of the job of getting the title and body of any article
#on that website 

for x in range(0,2):
    crawler.crawl(urlObj[x], titleObj[x], bodyObj[x])






        