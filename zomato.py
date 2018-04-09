import requests
from lxml import etree
key='03b8addd1ec273c95dcf077eaa05bee3'
print(key)
payload = {'key':key}
r=requests.get('https://www.zomato.com',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.findall("projects/asir1")
	for p in projects:
		print (p.text)
