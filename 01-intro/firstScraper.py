from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# try:
#     html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#     bs = BeautifulSoup(html, "html.parser")
#     print(bs.nonExistentTag)
# except HTTPError as e:
#     print(e)
#     #return break etc
# except URLError as e:
#     print(e)
# else:
#     print("it worked")
#     #continue program

#to check is the tag exists or not 
# try:
#     badContent = bs.nonExistingTag.anotherTag
# except AttributeError as e:
#     print('Tag was not found')
# else:
#     if badContent == None:
#         print ('Tag was not found')
#     else:
#         print(badContent)


#a better way of writing it
def getTitle(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, "html.parser")
        tag = bs.h1
    except HTTPError as e:
        return None
    except AttributeError as e:
        return None
    else:
        return tag

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if(title == None):
    print("couldnt be found")
else:
    print(title)
