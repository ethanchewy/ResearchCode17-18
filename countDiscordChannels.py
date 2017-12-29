'''
This script scrapes the top 6 discord public lists
and counts the total number of unique discord channels

https://discord.me/servers/1 
https://discordservers.com/ 
https://discordlist.me/
https://disboard.org/ 
https://discord-server.com/ 
https://discordlist.net/ 
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from collections import OrderedDict
import pandas as pd
import string

# The path works because I have moved the "chromedriver" file in /usr/local/bin
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
listofChannels=[]

#https://discord.me/servers/1
browser.get('https://discord.me/servers/1')

a = 0

#Use infinite loop since the total number of pages is unknown. 
#At least in jupyter notebooks, it'll stop when it can't find the "Next" button on the last page)
while True:
    names = browser.find_elements_by_class_name("server-name")
    for name in names:
        listofChannels.append(name.text)
    moveforward = browser.find_elements_by_xpath("//*[contains(text(), 'Next')]")[0]
    moveforward.click()
    print a
    a+=1
    time.sleep(3)
        
    
listofChannels

'''
Still in the works
#https://discordservers.com/
listofChannels2 = []
browser.get('https://discordservers.com/')

inputBox = browser.find_element_by_class("input")

#find class input
abc = list(string.ascii_lowercase)
for letter in abc:
    inputBox.clear()
    inputBox.send_keys(letter)
    inputBox.send_keys(Keys.ENTER)
    time.sleep(3)
    
    names = browser.find_elements_by_class_name("name")
    for name in names:
        listofChannels2.append(name.text)
        moveforward = browser.find_elements_by_xpath("//*[contains(text(), 'Next')]")[0]
        moveforward.click()
    #Solution to stale element issue since element changes from the original q element
    inputBox = browser.find_element_by_class("input")
'''

#Find Duplicates using Pandas library
cleanList = pd.unique(listofChannels).tolist()
cleanList

#Find number of discord channels
count = len(cleanList)
print count
