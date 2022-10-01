"""
coming back to this when I learn network programming
so I could process all the javascript


https://proscheduler.prometric.com/scheduling/searchAvailability 


select a test sponsor 
api link: https://scheduling.prometric.com/api/v1/Clients?isPublished=true 
authorization header goes with this
then OPTIONS request to api link + id of sponsor clientId=...

select a program

select a test
"""
import requests
from bs4 import BeautifulSoup

session = requests.Session()
param = {'authorization': "Bearer "}
header = {'sec-fetch-mode': 'cors', 'access-control-request-headers': 'authorization,sessionid', 'access-control-request-method': 'GET', 'origin': 'https://proscheduler.prometric.com', 'referer': 'https://proscheduler.prometric.com/', 'sec-fetch-site': 'same-site'}
s = session.get('https://scheduling.prometric.com/api/v1/Clients?isPublished=true', headers=param)
print("\n", s.cookies.get_dict())
s = session.options('https://scheduling.prometric.com/api/v1/Programs?clientId=IhODyPf46UypMSrDR10vJg&isPublished=true',headers=param)
# s = session.get('https://scheduling.prometric.com/api/v1/Programs?clientId=IhODyPf46UypMSrDR10vJg&isPublished=true', headers=param)
print(s.headers)
print("\n", s.cookies.get_dict())
soup = BeautifulSoup(s.text, "html.parser")
print(soup)
