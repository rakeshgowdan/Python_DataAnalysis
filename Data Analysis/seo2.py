import pyexcel as pe
import sqlite3
import pandas as pa
import matplotlib.pyplot as plot
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

conn = sqlite3.connect("Seo_DataBase.db")
def read_from_pyexcel():
    sheet = pe.get_sheet(sheet_number=0, file_name="C:\\Users\\Raksh\\PycharmProjects\\Data_Analysis\\Reader.xlsx")
    url = sheet.column_at(0).__getitem__(0)
    keywords = sheet.column[1]
    return keywords, url

def read_from_url(keywords, url):
    req = requests.get(url, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)AppleWebKit/537.36(KHTML,like Gecko)Chrome/35.0.1916.47 Safari/537.36'})
    soup = BeautifulSoup(req.content, 'html.parser')
    soupStrainer = SoupStrainer("a")
    print(soupStrainer)
    for content in soup(["script","style"]):
        content.extract()
        cont = soup.get_text()
        print(cont)
    lines = (line.strip() for line in cont.splitlines())
    l = []
    ctrlist = []
    for line in lines:
        l = line.split()
        #print(l)
    for word in l:
        if word in keywords:
            ctrlist.append(word)
           # print(ctrlist)
    lengthoflist = len(l)
    return (ctrlist, lengthoflist)


def insert_into_db(ctrlist, lengthoflist):
    ctr = 0
    li = []
    D = {}
    density = 0
    setofwords = set(ctrlist)
    listofwords = list(setofwords)
    for word in listofwords:
        ctr = ctrlist.count(word)
        D[word] = ctr
        density = (D[word] / lengthoflist) * 100
        li.append(density)
    dictlist = list(D.keys())
    for x in zip(dictlist, li):
        #conn.execute("create table words(word text,density numeric)")
        conn.execute("insert into ScrapData(name,density) values(?,?)", x)
    conn.commit()


def plot_graph():
    query = "SELECT * FROM ScrapData;"
    df = pa.read_sql_query(query, conn)
    df.plot(kind='bar', x='name', y='density')
    plot.show()
    plot.savefig('output.png')
    conn.close()

a,b = read_from_pyexcel()
#print(a,b)
c,d = read_from_url(a,b)
#print(c,d)
#insert_into_db(c,d)
#plot_graph()