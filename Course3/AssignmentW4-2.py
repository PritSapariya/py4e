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

position = 1
count = 1

url = input('Enetr - ')
while True :
    url = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(url, 'html.parser')

    tags = soup('a')
    for tag in tags :
        if position == 18 : 
            url = tag.get('href', None)
            break
        position = position + 1

    if count == 7 :
        print(url)
        break
    count = count + 1
    position = 1