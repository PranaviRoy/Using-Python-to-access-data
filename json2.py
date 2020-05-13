import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
incoming_data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(incoming_data)
total_sum = 0
for item in info['comments']:
    total_sum += int(item['count'])
print(total_sum)