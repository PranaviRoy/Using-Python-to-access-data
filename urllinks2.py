# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

Names = tags[position-1].contents[0] + ' '

for _ in range(count - 1):
    url = tags[position-1].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    Names += tags[position-1].contents[0] + ' '

#print("Sequence of Names:" + Names)
print("Last Name: " + tags[position-1].contents[0])