#Check hate word frequency in a list of messages.
#Uses NTLK and Hatebase libraries
#Graphs top ten occurences of hate words!


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

print difflib.get_close_matches("dyke", test123, 10, .5)"""

#python wrapper : https://github.com/DanielJDufour/hatebase

#Message is equal to each other

#print len(message)
#initiate lists to set length
frequency = []
versionsOfWord = []
for x in range(0, 1000):
    frequency.append(0)

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
    
    
    
totalNumberofWords = 0
for m in message:
    #print m
    totalNumberofWords += len(m)
    lower = m.lower()
    index = 0
    
    #Need to tokenize to get all frequencies
    for word in listofHatewords:
        listof_lower = lower.split(" ")
        similarWords = versionsOfWord[index]

        #matchesHate = difflib.get_close_matches(word, listof_lower, 1, .5)
        #https://docs.python.org/2/library/difflib.html
        #Else if check the NTLK forms of words
        #Check if there are versions of the word first though
        if word in lower or len(difflib.get_close_matches(word, listof_lower, 1, .5)) >= 1:
            frequency[index]+=1
        elif len(similarWords) > 0:
            found = False
            for a in similarWords:
                if a in lower or len(difflib.get_close_matches(a, listof_lower, 1, .5)) >= 1:
                    found = True
                    break
            
            if found is True:
                frequency[index]+=1
        
        #Increase index to make sense
        if index >= len(listofHatewords):
            print "Length error"
        index+=1

#check asterisk. 
#Get list of words
#Use difflib library => get_close_matches of words. Cutoff value
#Use NTLK
#Think about software filtering methods

print len(message)
print frequency



#Total mentions of words in posts
#=>Treats each word in every post as equal<=


#output list of hate words into text file
import simplejson
try:
    print listofHatewords
    f = open('listofhatewords.json', 'w')
    simplejson.dump(listofHatewords, f)
    f.close()
except NameError:
    print "Almost erased listofhatewords.json! Be careful!!!"



