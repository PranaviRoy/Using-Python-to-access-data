import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
xml = urllib.request.urlopen(url, context=ctx).read()
data = ET.fromstring(xml)

counts = data.findall('.//count')
total_sum = 0
for count in counts:
    total_sum += int(count.text)

print(total_sum)
