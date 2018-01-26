#Check hate word frequency in a list of messages.
#Uses NTLK and Hatebase libraries
#Graphs top ten occurences of hate words!

#ONLY DO ONCE
#DO NOT WASTE API CALLS
key = "ENTER_YOU_KEY_HERE"

from json import loads
from hatebase import HatebaseAPI

hatebase = HatebaseAPI({"key": key})
#"language": "eng"
pagenumber = 1
responses = []

#Loads top 1000 results
while pagenumber <= 11:
    filters = {"country":"US", "page": str(pagenumber)}
    output = "json"
    query_type = "vocabulary"
    response = hatebase.performRequest(filters, output, query_type)

    # convert to Python object
    responses.append(loads(response))
    pagenumber += 1
    
print "Done getting API results"

#Process Hate Words
data = []
for r in responses:
    data.append(r["data"])
#print len(data)
listofHatewords = []

#print len(data)
for z in data:
    for a, v in z.iteritems():
        for b in v:
            listofHatewords.append(b["vocabulary"])
print listofHatewords
listofHatewords = list(OrderedDict.fromkeys(listofHatewords))
print len(listofHatewords)


#Check hate word frequency



#Use ntlk and hatelibrary
#http://www.nltk.org/book/ch01.html
#hatelibrary sign up for API: https://www.hatebase.org/login_register/registration_success
#a29261266be5f2798d7d08bac9bb70d6
#Daily Limit = 100 <=
#But I can always get a new key

#Do ntlk stuff after

#Two types of graphs: one for frequency among all words and frequency among all posts.

#NOTE
"""
If you publish work that uses NLTK, please cite the NLTK book as follows:

Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
"""


#print data
#print listofHatewords
#print len(listofHatewords)
#print listofHatewords

"""#test difflib

test123 = "dyke d*ke dy*e dnke"

test123 = test123.split(" ")

print difflib.get_close_matches("dyke", test123, 10, .75)"""

#python wrapper : https://github.com/DanielJDufour/hatebase

#Message is equal to each other

#print len(message)
#initiate lists to set length
frequency = []
versionsOfWord = []
#frequencyID = []
frequencyTime = []
#Index of original message list
listmessageID = []
listauthors = []
frequencyIndex = []
for x in range(0, 1000):
    frequency.append(0)

"""
for x in range(0, 1000):
    frequencyID.append([])
"""
for x in range(0, 1000):
    listmessageID.append([])
for x in range(0, 1000):
    listauthors.append([])

for x in range(0, 1000):
    frequencyTime.append([])
for x in range(0, 1000):
    frequencyIndex.append([])
    
for x in range(0, 1000):
    versionsOfWord.append([])

#NTLK 
#FROM: https://stackoverflow.com/a/45158719/4698963
from nltk.corpus import wordnet as wn
#We'll store the derivational forms in a set to eliminate duplicates
index2 = 0
for word in listofHatewords:
    forms = set()
    for happy_lemma in wn.lemmas(word): #for each "happy" lemma in WordNet
        forms.add(happy_lemma.name()) #add the lemma itself
        for related_lemma in happy_lemma.derivationally_related_forms(): #for each related lemma
            forms.add(related_lemma.name()) #add the related lemma
        versionsOfWord[index2] = forms
    index2 += 1
print len(versionsOfWord)

"""#Measure time of loop
import time
start = time.clock() """

#old code
#Time for 254776 messages: 3323.288668 seconds
#Time for all 2979089 result minimum: 10.7942016982 hours

#new code
#Time for 1000 messages: 13.301362 seconds
#Time for 2979089 messages: 11.007205894227 hours

#new new code
#Time for 1000 messages: 11.202224 second
#Time for 2979089 messages: 9.2701173038712 hours
    
totalNumberofWords = 0
counter = 0
print len(message)
print len(messageID)
print len(timestamps)
for m, m_id, date, a_id in zip(message, messageID, timestamps, authorID):
    #print m
    totalNumberofWords += len(m)
    lower = m.lower()
    index = 0

    
    
    if counter%100000==0:
        print counter
    #print counter
    #Need to tokenize to get all frequencies
    for word in listofHatewords:
        wordLowered = word.lower()
        listof_lower = lower.split(" ")
        similarWords = versionsOfWord[index]

        #matchesHate = difflib.get_close_matches(word, listof_lower, 1, .5)
        #https://docs.python.org/2/library/difflib.html
        #Else if check the NTLK forms of words
        #Check if there are versions of the word first though
        #TOOK out "word in lower" since it was inaccurate
        if wordLowered in listof_lower or len(difflib.get_close_matches(wordLowered, listof_lower, 1, .75)) >= 1:
            frequency[index]+=1
            frequencyIndex[index].append(counter)
            #frequencyID[index].append(str(m_id) + " " + m)
            frequencyTime[index].append(date)
            listmessageID[index].append(m_id)
            listauthors[index].append(a_id)
        elif len(similarWords) > 0:
            #found = False
            for a in similarWords:
                aLowered = a.lower()
                if aLowered in listof_lower or len(difflib.get_close_matches(aLowered, listof_lower, 1, .75)) >= 1:
                    #found = True
                    frequency[index]+=1
                    frequencyIndex[index].append(counter)
                    #frequencyID[index].append(str(m_id) + " " + m)
                    frequencyTime[index].append(date)
                    listmessageID[index].append(m_id)
                    listauthors[index].append(a_id)
                    #print "test" + str(counter)
                    break 
        #Increase index to make sense
        if index >= len(listofHatewords):
            print "Length error"
        
        index+=1
    counter += 1

#check asterisk. 
#Get list of words
#Use difflib library => get_close_matches of words. Cutoff value
#Use NTLK
#Think about software filtering methods

print "All Done" + str(len(message))
#print frequency



#Total mentions of words in posts
#=>Treats each word in every post as equal<=

#Process data
jsonList = []

for i in range(0,1000):
    jsonList.append({'hateword': listofHatewords[i], 'messageID': listmessageID[i], 'authorID':listauthors[i], 'frequency': frequency[i], 'frequencyIndex':frequencyIndex[i], 'frequencyTime':frequencyTime[i]})
    
#print(json.dumps(jsonList, indent = 1))

#Put to file
import simplejson
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
try:
    f = open(ChannelName + 'Allfrequencies'  + str(timestr) +'.json', 'w')
    simplejson.dump(jsonList, f)
    f.close()
except NameError:
    print "Almost erased" + ChannelName + "Allfrequencies.json! Be careful!!!"
