'''
Created on Dec 1, 2013

@author: konstantinos kostis , <kekostis@gmail.com>
'''

from Email import *
import math

"""
this class will take a list of e-mails and will try to extract a list of features 
"""

class FeatureSelection(object):
    
    def __init__(self,emails):
        self.emails = emails
        self.num_spams = 0
        self.num_hams = 0
        self.prob_spam = 0
        self.prob_ham = 0
        self.Entropy = 0
        self.setNumSpams()
        self.setNumHams()
        self.setSpamProbability()
        self.setHamProbability()
        self.calculateEntropy()
        self.allWords = []
        self.wordInSpams = [] #stores how many times a word exists in all spams
        self.wordInHams = []
        self.wordInAll = []
        self.MI = {} #will contain the mutual information of every word
        self.sortedMI = []
    
    def setNumSpams(self):
        for e in self.emails:
            if e.getCategory() == "SPAM":
                self.num_spams += 1
          
    def getNumSpams(self):
        return self.num_spams
    
    def setNumHams(self):
        for e in self.emails:
            if e.getCategory() == "HAM":
                self.num_hams += 1
    
                    
    def getNumHams(self):
        return self.num_hams
    
    """find the SPAM probability"""
    def setSpamProbability(self):
        self.prob_spam = (float)(self.getNumSpams())/len(self.emails)
        
    def getSpamProbability(self):
        return self.prob_spam
    
    """find the ham probability"""
    def setHamProbability(self):
        self.prob_ham = (float)(self.getNumHams())/len(self.emails)
    
    def getHamProbability(self):
        return self.prob_ham
    
    """calculate entropy"""
    def calculateEntropy(self):
        self.Entropy = -self.getSpamProbability()*math.log(self.getSpamProbability(),2)-self.getHamProbability()*math.log(self.getHamProbability(),2)
    
    def getEntropy(self):
        return self.Entropy
    
    
    def selectFeatures(self):
        print "starting selecting features..."
        #put all unique words of all e-mails in a list
        for e in self.emails:
            wordsOfEmail = list(e.getWordsDictionary().keys())
            for w in wordsOfEmail:
                if w not in self.allWords:
                    self.allWords.append(w)
        #find how many times  a word appears in spams , in hams and in all messages 
        for w in self.allWords:
            times_inSpams = 0
            times_inHams = 0
            times_inAll = 0
            for e in self.emails:
                wordsDictionaryOfEmail = e.getWordsDictionary()
                if w in wordsDictionaryOfEmail:
                    if e.getCategory() == "SPAM":
                        times_inSpams = times_inSpams+wordsDictionaryOfEmail[w]
                    else:
                        times_inHams = times_inHams+wordsDictionaryOfEmail[w]
            times_inAll = times_inSpams + times_inHams
            self.wordInSpams.append(times_inSpams)
            self.wordInHams.append(times_inHams)
            self.wordInAll.append(times_inAll)
        
        for w in self.allWords:
            #pr_x_1 is the Pr(w=EXISTS)
            pr_x_1 = (float)(self.wordInAll[self.allWords.index(w)])/sum(self.wordInAll)
            #pr_x_0 is Pr(w=DOES NOT EXIST)
            pr_x_0 = 1-pr_x_1
            
            hams_containW = 0
            hams_NO_containW = 0
            spams_containW = 0
            spams_NO_containW = 0
            for e in self.emails:
                if e.getCategory() == "HAM":
                    if e.contains(w) == True:
                        hams_containW += 1
                    else:
                        hams_NO_containW += 1
                else:
                    if e.contains(w) == True:
                        spams_containW += 1
                    else:
                        spams_NO_containW += 1
            #print "Word: %s \t hams_w: %i \t hams_no_w: %i \t spams_w: %i \t spams_no_w: %i" % (w,hams_containW,hams_NO_containW,spams_containW,spams_NO_containW)
            #calculate some probabilities
            
            #pr_x_1_HAM is Pr(w=EXISTS,c=HAM) = Pr(HAM)*Pr(w=EXISTS|C=HAM) = Pr(HAM)*((1+hams containing w)/(2+all hams))
            pr_x_1_HAM = self.getHamProbability()*((float)(1+hams_containW)/(2+self.getNumHams()))
            #print "Pr(w=EXISTS,c=HAM) = %f " % (pr_x_1_HAM)
            term_1_HAM = pr_x_1_HAM*math.log(pr_x_1_HAM/(pr_x_1*self.getHamProbability()))
            #print "sum(w=EXISTS,c=HAM) = %f " % (term_1_HAM)
            #pr_x_1_SPAM is Pr(w=EXISTS,c=SPAM) = Pr(SPAM)*Pr(w=EXISTS|C=SPAM) = Pr(SPAM)*((1+spams containing w)/(2+all spams))
            pr_x_1_SPAM = self.getSpamProbability()*((float)(1+spams_containW)/(2+self.getNumSpams()))
            term_1_SPAM = pr_x_1_SPAM*math.log(pr_x_1_SPAM/(pr_x_1*self.getSpamProbability()))
            
            #pr_x_0_HAM is Pr(w=NO_EXISTS,c=HAM) = Pr(HAM)*Pr(w=NO_EXISTS|C=HAM) = Pr(HAM)*((1+hams no containing w)/(2+all hams))
            pr_x_0_HAM = self.getHamProbability()*((float)(1+hams_NO_containW)/(2+self.getNumHams()))
            term_0_HAM = pr_x_0_HAM*math.log(pr_x_0_HAM/(pr_x_0*self.getHamProbability()))
            
            #pr_x_0_SPAM is Pr(w=NO_EXISTS,c=SPAM) = Pr(SPAM)*Pr(w=NO_EXISTS|C=SPAM) = Pr(SPAM)*((1+spams no containing w)/(2+all spams))
            pr_x_0_SPAM = self.getSpamProbability()*((float)(1+spams_NO_containW)/(2+self.getNumSpams()))
            term_0_SPAM = pr_x_0_SPAM*math.log(pr_x_0_SPAM/(pr_x_0*self.getSpamProbability()))
            
            mi = term_1_HAM+term_1_SPAM+term_0_HAM+term_0_SPAM
            self.MI[w] = mi
        self.sortedMI = sorted(self.MI.items(),key=lambda t : t[1],reverse=True)
        #create a file to store the 250 first features
        featuresFileDescriptor = open("features.txt","w")
        num = 0
        for x in self.sortedMI:
            if(num >= 250):
                break
            featuresFileDescriptor.write(x[0]+"\n")
            featuresFileDescriptor.flush()
            num += 1
        featuresFileDescriptor.close()
        print "Features are selected!!!"

            
    
    
            