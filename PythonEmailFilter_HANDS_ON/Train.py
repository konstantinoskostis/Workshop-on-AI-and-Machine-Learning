'''
Created on Dec 1, 2013

@author: konstantinos kostis , <kekostis@gmail.com>
'''

""" This script will read all the emails and it will train the classifier """


import os
from Email import *
from FeatureSelection import *
from NaiveBayesClassifier import *

trainPath = "dataset"
trainSet_emails = []

#create an email for every file we read
for f in os.listdir(trainPath):
    fileName = trainPath+'/'+f
    e = Email()
    if "spm" in fileName:
        e.setCategory("SPAM")
    else:
        e.setCategory("HAM")
    e.read(fileName)
    #insert the email we created to a collection of emails
    trainSet_emails.append(e)

#select features from our training set(automatic feature selection)
fs = FeatureSelection(trainSet_emails)
fs.selectFeatures()

#create a naive bayes classifier and train it
nb = NaiveBayesClassifier()
nb.setEmails(trainSet_emails)
nb.train()