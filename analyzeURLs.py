from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib, json
from pprint import pprint
import time

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
	
# Path = where the "chromedriver" file is
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
browser.get('https://www.reddit.com/reddits')

#Get info on each search term
inputBox = browser.find_element_by_name("q")
info = []
for channel in subReddits:
    inputBox.clear()
    inputBox.send_keys(channel)
    inputBox.send_keys(Keys.ENTER)
    time.sleep(3)
    #find element 
    info.append(browser.find_elements_by_class_name("md")[1].text)
    #Solution to stale element issue since element changes from the original q element
    inputBox = browser.find_element_by_name("q")
	
#Get data for Snippets
snippets=[]
for a in data:
	for b in a['results']:
		snippets.append(b['snippet'])
	
import json
import pandas as pd
#Print out data in a nice spreadsheet
arrays = zip(links, subReddits, timestamp, info, snippets)
df = pd.DataFrame(data=arrays)
df

#Convert to csv file
df.to_csv("December2016November2017discordgg.csv", encoding='utf-8', index=False)
