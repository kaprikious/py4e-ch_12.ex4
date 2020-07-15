# http://py4e-data.dr-chuck.net/comments_42.html
#python3 Testt.py
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos = int(input("Enter position:"))-1
count = int(input("Enter count:"))

#print('TAG:', tag)
#('URL:', tag.get('href', None))
#print('Contents:', tag.contents[0])
#print('Attrs:', tag.attrs)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

Sq = list()
tags = soup('span')
for i in range(count):
    link = tags[pos].get('href', None)
#Retrieving link
    Sq.append(tags[pos].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('span')
    link = tags[pos].get('href', None)

print(Sq[-1])
