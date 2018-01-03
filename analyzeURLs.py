'''
This script is for processing Google Scraping data I collected with my GoogleScraper modified scraper. 
See Github repos & blog for more details
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib, json
from pprint import pprint
import time

#Comment out if you are collecting for the first time
#Import CSV data so that you don't have to recollect all the data again
'''
colnames = ['links', 'subReddits', 'timestamp', 'info', 'snippets']
data = pandas.read_csv('December2016November2017discordgg.csv', names=colnames)
links = data.links.tolist()
subReddits = data.subReddits.tolist()
timestamps = data.timestamp.tolist()
#data.info is another function!
infos = data["info"].tolist()
snippets = data.snippets.tolist()
'''
#Note that lists' first element is the number indicating the position of the column in the csv file

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

#Get data for Snippets
snippets=[]
for a in data:
	for b in a['results']:
		snippets.append(b['snippet'])

#Process data to get subreddit page and description
#Gathers as much info as possible for subreddit info
#Subreddits have different CSS so be careful
#Notes: https://docs.google.com/document/d/1pegankZVLFGLRIqEpfdQwilZ_T-cQkm7dyeQdOltFgU/edit
#THIS CODE ASSUMES THE BROWSER YOU ARE USING IS NOT LOGGED INTO REDDIT 
originalPostContent = []
titleOfRedditPost = []
typeOfPost = []
authorLink = []

#list of lists of all the comments of the post: https://stackoverflow.com/questions/11487049/python-list-of-lists
#Will not do right now due to time constraints
completeThread = []

#Does Google even scrape Reddit comments? Analyzed just in case.

#Comments look like => https://www.reddit.com/r/science/comments/7n2zqt/study_of_550_college_students_who_had_used_or/dryyzir/
#8th part of regex

#For removing links remember to remove all data points
#For loop to process each link

#Uncomment this if you are analyzing new data and not importing.
for a, b, c in zip(links, snippets, timestamp):
#for a, b, c, d, e in zip(links, snippets, timestamp, subReddits, info):
    
    #Try else loop to see if the link is actually a comment or post 
    #If not either, it's not reliable since it's probs related to a wiki page
    #Thus, if it's something like a wiki page, that means the timestamp could be incorrect
    try:
        part = a.split('/')[5]
        print part
        browser.get(a)
        
        '''
        Try to see if it's a comment.
        Process Comment in its entirety if so.
        Find HTML element.

        '''
        
        try:
            partOfComment = a.split('/')[8]
            typeOfPost.append("Comment")
            elem = browser.find_elements_by_class_name("commentarea")[0]
            elem2 = elem.find_elements_by_class_name("sitetable")[0]
            content = elem2.find_elements_by_class_name("thing")[0]      
            theComment = content.find_elements_by_class_name("entry")[0]
            contentOfComment = theComment.find_elements_by_class_name("usertext")[0].text
            byLine = theComment.find_elements_by_class_name("tagline")[0]
            authorHREF = byLine.find_elements_by_tag_name("a")[1].get_attribute("href")

            titleOfRedditPost.append("")
            originalPostContent.append(contentOfComment)
            authorLink.append(authorHREF)
            
        #Process Post in its entirety
        except IndexError:
            #Temp solution to "Wiki" Issue
            #Checks if it is a wiki page or just an empty string
            if "wiki" in part or not part:
                print "Removed that!"
                links.remove(a)
                snippets.remove(b)
                timestamp.remove(c)
                #Remove bottom two lines of code if not importing already collected data
                #subReddits.remove(d)
                #info.remove(e)
            else: 
                typeOfPost.append("Post")

                #Isloate elements and get texts
                elem = browser.find_elements_by_class_name("entry")[0]
                content = elem.find_elements_by_class_name("expando")[0].text      
                frontmatter = elem.find_elements_by_class_name("top-matter")[0]
                title = frontmatter.find_elements_by_class_name("title")[0].text
                byLine = frontmatter.find_elements_by_class_name("tagline")[0]
                authorHREF = byLine.find_elements_by_tag_name("a")[0].get_attribute("href")

                #Append to correct indice
                titleOfRedditPost.append(title)
                authorLink.append(authorHREF)
                originalPostContent.append(content)
    except IndexError:
        links.remove(a)
        snippets.remove(b)
        timestamp.remove(c)
        #Remove bottom two lines of code if not importing already collected data
        #subReddits.remove(d)
        #info.remove(e)
    time.sleep(3)

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
    try:
        elem = browser.find_elements_by_class_name("md")[1]
        info.append(elem)
    except IndexError:
        info.append("")
    #Solution to stale element issue since element changes from the original q element
    inputBox = browser.find_element_by_name("q")

	
import json
import pandas as pd
#Print out data in a nice spreadsheet
arrays = zip(links, subReddits, timestamp, info, snippets)
df = pd.DataFrame(data=arrays)
df

#Convert to csv file
df.to_csv("December2016November2017discordgg.csv", encoding='utf-8', index=False)
