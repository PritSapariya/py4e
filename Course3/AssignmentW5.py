import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

count = 0
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)
    lst = tree.findall('.//count')
    
    for item in lst :
        print(item.text)
        sum = sum + int(item.text)
        count = count + 1
    print('Count: ', count)
    print('Sum: ', sum)
            