import requests
from bs4 import BeautifulSoup as BS

page = 1
href = []

r = requests.get('https://stopgame.ru/topgames?rating=izumitelno&p=' + str(page))
soup = BS(r.content, 'html.parser')

urlka = soup.find_all('div', class_='image slanted')
ind = urlka[0].attrs['style'].find('https')
print(urlka[0].attrs['style'][ind:-1])




