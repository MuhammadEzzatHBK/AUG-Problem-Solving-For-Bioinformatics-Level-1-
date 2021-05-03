import requests

x = requests.get('https://w3schools.com/python/demopage.htm')
print(x. text, '\n')
#Check If the Page exists
if x.status_code == 200:
    print('\tSuccess!')
elif x.status_code == 404:
    print('\tNot Found!')