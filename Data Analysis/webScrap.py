from bs4 import BeautifulSoup
import requests

url = 'http://www.thehindu.com/opinion/op-ed/Does-Beijing-really-want-to-ldquobreak-uprdquo-India/article16875298.ece'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
for content in soup.select("[id^='content-body-'] p"):
    print(content.text)