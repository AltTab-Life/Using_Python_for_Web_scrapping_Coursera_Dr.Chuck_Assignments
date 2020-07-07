import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url ="http://py4e-data.dr-chuck.net/comments_744843.xml"
uh = urllib.request.urlopen(url)
sum=0

data = uh.read().decode()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
#print('Counts>> ',counts[4])

for i in range(len(counts)):
    sum = sum + int(counts[i].text)

print('Sum is >>', sum)