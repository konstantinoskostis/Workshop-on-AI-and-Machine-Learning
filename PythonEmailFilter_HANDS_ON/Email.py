'''
Created on Dec 1, 2013

@author: konstantinos kostis , <kekostis@gmail.com>
'''

import collections

"""
This class represents an Email
"""


class Email(object):
    """ an empty constructor """

    def __init__(self):
        self.content = "" # content is the text in the body of an email
        self.category = " " # the category of an email is HAM(good)) or SPAM(bad)
        self.wordsDictionary = {} # this dictionary will hold all the unique words along with their frequency in the content
        self.featureVector = [] #a vector that contains 1 or 0 in every position

    """ set the content variable """

    def setContent(self, content):
        self.content = content

    """ get the content """

    def getContent(self):
        return self.content

    """ set the category variable """

    def setCategory(self, category):
        self.category = category

    """ get the category """

    def getCategory(self):
        return self.category

    """ get the dictionary """

    def getWordsDictionary(self):
        return self.wordsDictionary

    def getName(self):
        return self.name

    """ read an email given its path """
    ''' COMPLETE THE METHOD!!! '''

    def read(self, fileName):
        #save fileName to variable name

        #open file

        #read lines of file and add line to the content

        #close file

        #preprocess content of file

        #all letters to lower case

        # find all unique words and their frequency
        pass

    '''removes some special characters'''

    def preprocess(self):
        toRemove = [".", ",", "(", ")", "[", "]"]
        for element in toRemove:
            self.content = self.content.replace(element, " ")

    """put to dictionary every word along with its frequency"""

    def fillDictionary(self):
        listOfWords = self.content.split() #split on empty string and return every non-empty string
        self.wordsDictionary = collections.Counter(listOfWords) #returns unique words with their frequency

    """returns True if w exists in this email"""

    def contains(self, w):
        if self.getWordsDictionary().has_key(w):
            return True
        return False

    """Transforms an email to a vector"""

    def setFeatureVector(self, features):
        for feature in features:
            if self.contains(feature) is True:
                self.featureVector.append(1);
            else:
                self.featureVector.append(0)

    def getEmailVector(self):
        return self.featureVector
