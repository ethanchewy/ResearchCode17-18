import urllib, json
from pprint import pprint

#Load Json
data = json.load(open('discordgg/December2016November2017.json'))

#Get Only Links from JSON
links=[]

for a in data:
	for b in a['results']:
		links.append(b['link'])
		#pprint(b['link'])
#Process time stamps correctly for data. 
#Note that some are in the general data instead of the correct time slot
timestamp=[]
for a in data:
	for b in a['results']:
		#Fix why none is not working
		#shitty workaround with length of 4?
		if 'None' in b['time_stamp']:
			timestamp.append(b['snippet'][0:12])
		else:
			timestamp.append(b['time_stamp'][0:12])
#Slice to appropriate date from original data
#for stamp in timestamp:
#Pattern => 11 or 12 characters. the next character is a space.
#Better way is to find 2016 or 2017 and then slice till that point

for what in timestamp:
	pprint(what)

#Process data using regex to get subreddits
subReddits=[]
for y in links:
	subReddits.append(y.split('/')[4])
	#pprint(y.split('/')[4])

#Categorize subReddits

#pandas dataframe
bothArrays = zip(links, subReddits, timestamp)
df = pd.DataFrame(data=bothArrays)
