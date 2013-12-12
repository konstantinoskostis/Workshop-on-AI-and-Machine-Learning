'''
Created on Dec 1, 2013

@author: konstantinos kostis , <kekostis@gmail.com>
'''

import os
from Email import *
from NaiveBayesClassifier import *

#read test files/emails
testPath = "test"
testEmails = []

for testEmail in os.listdir(testPath):
    fileName = testPath+'/'+testEmail
    e = Email()
    e.read(fileName)
    #insert the email we created to a collection of emails
    testEmails.append(e)

#create a NaiveBayesClassifier object
NBC = NaiveBayesClassifier()
results = open("results.txt","w")
#classify every email
for testEmail in testEmails:
    results.write(testEmail.getName()+ " " +NBC.classify(testEmail)+"\n")
    results.flush()
    #print "%s \t %s" % (testEmail.getName(),NBC.classify(testEmail))
results.close()
