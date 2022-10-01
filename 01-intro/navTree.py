from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

def navTree(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, "html.parser")
    except HTTPError or URLError or AttributeError:
        return None
    else:
        return bs
    


content = navTree('http://www.pythonscraping.com/pages/page3.html')
#prints all of the siblings
# for con in content.find('table', {'id':'giftList'}).tr.next_siblings:
#     print(con)

#finding all images using regex
for con in content.find_all("img", {'src': re.compile('\.\./img/gifts/img.*\.jpg')}):
    print(con)
    print(con.attrs) #returns a dictionary of all the attributes of that tag
    print(con.attrs['src']) #returns content of the attributes of that tag


