import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    count = 0
    sum = 0
    
    url = input('Enter Location: ')
    print('Retrieving', url)
    handle = urllib.request.urlopen(url, context=ctx)
    
    data = handle.read()
    print('Retrieved', len(data),'characters')

    info = json.loads(data)
    lst = info['comments']

    for item in lst:
        count = count + 1
        sum = sum + item['count']
    
    print(count)
    print(sum)