import urllib, json
from pprint import pprint

#Load Json
data = json.load(open('discordgg/November2015December2016.json'))

#Get Only Links from JSON
links=[]
for a in data:
	for b in a['results']:
		links.append(b['link'])
		pprint(b['link'])

#Process data using urllib library
