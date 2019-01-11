from bs4 import BeautifulSoup
from urllib.request import urlopen
url="https://www.google.com/"
html=urlopen(url)
soup = BeautifulSoup(html,'html.parser')
# create a new bs4 object from the html data loaded
for script in soup(["script", "style"]):
# remove all javascript and stylesheet code
	     script.extract()
# get text
text = soup.get_text()
print(text)
# break into lines and remove leading and trailing space on each
print(text.split())


