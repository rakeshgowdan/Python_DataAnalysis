import requests
from bs4 import BeautifulSoup
data=requests.get('https://www.w3schools.com/tags/tag_table.asp')
soup=BeautifulSoup(data.text,'html.parser')
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td.text)

