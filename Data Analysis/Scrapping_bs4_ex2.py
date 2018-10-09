import requests
from bs4 import BeautifulSoup
data=requests.get('https://umggaming.com/leaderboards')
soup=BeautifulSoup(data.text,'html.parser')
leaderBoard=soup.find('table',{'id':'leaderboard-table'})
tbody=leaderBoard.find('tbody')
for tr in tbody.find_all('tr'):
    #getting only places inside tr at position 0s
    place=tr.find_all('td')[0].text.strip()
    userName = tr.find_all('td')[1].find_all('a')[1].text.strip()
    xp = tr.find_all('td')[3].text.strip()

    print(place,userName,xp)
