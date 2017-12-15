import urllib, json
from pprint import pprint

#Load Json
data = json.load(open('discordgg/November2015December2016.json'))

#Get Only Links from JSON
links=[]
for a in data:
	for b in a['results']:
		links.append(b['link'])
		#pprint(b['link'])

#Process data using regex to get subreddits
subReddits=[]

for y in links:
	subReddits.append(y.split('/')[4])
	pprint(y.split('/')[4])

