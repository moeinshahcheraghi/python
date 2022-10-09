import requests
from bs4 import BeautifulSoup
from pyfiglet import Figlet
f = Figlet(font='slant')
print (f.renderText('Exchange rate '))
r = requests.get('https://www.tgju.org/')
soup = BeautifulSoup(r.text , 'html.parser')


val = soup.find_all('td')
res1 = val[2]
res2 = val[12]
res3 = val[18]
print ('The price of a coin today is', res1.text)
print()
print ('The dollar price today is', res2.text)
print()
print ('The price of gold today is', res3.text)
print()
