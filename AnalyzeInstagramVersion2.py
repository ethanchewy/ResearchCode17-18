from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from matplotlib.pyplot import hist
from urllib2 import Request, urlopen
import json
from datetime import date, datetime
import matplotlib.dates as mdates

import time

browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
url = "http://ligaviewer.com/discordapp"
browser.get(url)

#Click :Load more" once, then proceed

#Scroll all the way to the bottom
#440/20 = 22 =>^ 25
for i in range(1,25):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    
url = []
likes = []
comments = []
description = []
date = []
main = browser.find_element(By.XPATH, '//div[@class="media-list row"]')

#all_posts = main.find_elements(By.XPATH, '//div[@class="media-item col-xs-12 col-sm-6 col-md-4"]')
all_posts = main.find_elements(By.XPATH, '//div')

for i in all_posts:
    print main.find_elements(By.XPATH, '//div[@class="media-item__inner"]')[0].text

for i in xrange(len(all_posts)):
    blob = all_posts[i].find_element(By.XPATH, '//div[@class="media-item__inner"]')
    
    image = blob.find_element(By.XPATH, '//div[@class="media-item__img"]')
    currentURL = image.find_element(By.XPATH, 'a').get_attribute("href")
    url.append(currentURL)

    #//p[preceding::center/h3 and following::a[@href="index.htm"]]
    elem1 = blob.find_element(By.XPATH, '//div[@class="media-item__info"]')
    elem2 = elem1.find_element(By.XPATH, '//div[@class="media-item__info-right"]')
    rightSide = elem2.text.split(" ")
    currentLikes = rightSide[0]
    likes.append(currentLikes)

    currentComments = rightSide[1]
    comments.append(currentComments)

    ahhhhhh =  blob.find_element(By.XPATH, '//div[@class="media-item__description"]')                            
    currentDescription = ahhhhhh.find_element(By.XPATH, '//div[@class="media-item__text"]').text
    #elem3 = elem1.find_element(By.XPATH, '//div[@class="media-item__info-right"]')
    #following i[@class="comment"]]
    description.append(currentDescription)

    currentDate = ahhhhhh.find_element(By.XPATH, '//div[@class="media-item__date"]').text
    date.append(currentDate)



