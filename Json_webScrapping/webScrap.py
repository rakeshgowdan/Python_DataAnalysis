from urllib.request import urlopen
url="https://www.google.com/"
file=urlopen(url)
print(file.read())