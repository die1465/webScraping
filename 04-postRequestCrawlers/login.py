import requests

parameters = {"username": "eagle", "password": "password"}
r = requests.post('https://pythonscraping.com/pages/cookies/welcome.php', parameters)
print("cookies are :")
print(r.cookies.get_dict())
print("going to profile page...")
profilePage = requests.get('http://pythonscraping.com/pages/cookies/profile.php',
                            cookies=r.cookies)
print(profilePage.text)

print('-'*20, "using sessions", '-'*20)
session = requests.Session() #keeps track of session information like all cookies
#i dont have to send it with every request, just like a normal browser

s = session.post('https://pythonscraping.com/pages/cookies/welcome.php', parameters)
print("cookies are :")
print(s.cookies.get_dict())
print("going to profile page...")
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)