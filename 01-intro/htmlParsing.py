from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getContent(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, "html.parser")
        #the lines spoken by characters in the story are in red,
        #whereas the names of characters are in green.
        names = bs.find_all("span", {'class':'green'})

    except HTTPError or URLError or AttributeError:
        return None
    else:
        return names
    
content = getContent("http://www.pythonscraping.com/pages/warandpeace.html")
if(content == None):
    print("not found")
else:
    for name in content:
        print(name.get_text())