'''
Created on Dec 1, 2013

@author: konstantinos kostis , <kekostis@gmail.com>
'''

class NaiveBayesClassifier(object):
    
    def __init__(self):
        #initialize the HAM probability (PR_HAM) to zero
        self.PR_HAM = 0
        
        #initialize the SPAM probability (PR_SPAM) to zero
        self.PR_SPAM = 0
        
        #initialize a list(PR_EXISTS_HAM) to hold the Pr(x=1|C=HAM)
        self.PR_EXISTS_HAM = []
        
        #initialize a list(PR_NO_EXISTS_HAM) to hold the Pr(x=0|C=HAM)
        self.PR_NO_EXISTS_HAM = []
        
        #initialize a list(PR_EXISTS_SPAM) to hold the Pr(x=1|C=SPAM)
        self.PR_EXISTS_SPAM = []
        
        #initialize a list(PR_NO_EXISTS_SPAM) to hold the Pr(x=0|C=SPAM)
        self.PR_NO_EXISTS_SPAM = []
        
        #initialize a list to hold the features
        self.features = []
    
    
    """sets all the emails"""
    def setEmails(self,emails):
        self.emails = emails
        #initialize the num_spams to zero
        self.num_spams = 0
        #initialize the num_hams to zero
        self.num_hams = 0
        #count the SPAM emails and the HAM emails
        for email in self.emails:
            if email.getCategory() == "SPAM":
                self.num_spams += 1
            else:
                self.num_hams += 1
        
            
    """returns all emails"""
    def getEmails(self):
        return self.emails
    
    """loads features from a file"""
    def loadFeatures(self):
        #open file
        featuresDescriptor = open("features.txt","r")
        #load every line to features[]
        self.features = featuresDescriptor.read().splitlines()
        #close file 
        featuresDescriptor.close()
    
    def getFeatures(self):
        return self.features
    
    def getEmailVectors(self):
        return self.emailVectors
    
    """
    train the classifier,  we need to learn P(X|C) where X is a vector and c is a category
    for every feature calculate Pr(x=1|C=HAM),Pr(x=0|C=HAM),Pr(x=1|C=SPAM), Pr(x=0|C=SPAM)
    """
    def train(self):
        #initialize a list(emailVectors) that will hold every transformed email
        self.emailVectors = []
        
        #load the features - call the method
        self.loadFeatures()
        
        #transform every email to a vector and append the vector to email vectors[]
        for email in self.emails:
            email.setFeatureVector(self.features)
            self.emailVectors.append(email.getEmailVector())
    
        #for every feature(use index-based for loop)
        for featureIndex in range(0,len(self.features)):            
            #init a counter that indicates how many times aFeature exists in HAM messages
            hams_contain_Feature = 0
            #init a counter that indicates how many times aFeature does not exist in HAM messages
            hams_no_contain_Feature = 0
            #init a counter that indicates how many times aFeature exists in SPAM messages
            spams_contain_Feature = 0
            #init a counter that indicates how many times aFeature does not exist in SPAM messages
            spams_no_contain_Feature = 0
            
            #for every emailVector(use index-based for loop)
            for emailVectorIndex in range(0,len(self.emailVectors)):
                #get the current email
                current_email = self.getEmails()[emailVectorIndex]
                #get current emailVector
                current_emailVector = self.getEmailVectors()[emailVectorIndex]
                #if the current email is HAM
                if current_email.getCategory() == "HAM":
                    #if the current feature exists in the current email add one to appropriate counter
                    if current_emailVector[featureIndex] == 1 :
                        hams_contain_Feature += 1
                    #else if the current feature does not exist in the current email add one to appropriate counter
                    else:
                        hams_no_contain_Feature += 1
                #else if the current email is SPAM
                else:
                    #if the current feature exists in the current email add one to appropriate counter
                    if current_emailVector[featureIndex] == 1 :
                        spams_contain_Feature += 1
                    #else if the current feature does not exist in the current email add one to appropriate counter
                    else:
                        spams_no_contain_Feature += 1
                  
            # calculate and save Pr(x=1|C=HAM)
            self.PR_EXISTS_HAM.append((float)(1+hams_contain_Feature)/(2+self.num_hams))
            # calculate and save Pr(x=0|C=HAM)
            self.PR_NO_EXISTS_HAM.append((float)(1+hams_no_contain_Feature)/(2+self.num_hams))
            # calculate and save Pr(x=1|C=SPAM)
            self.PR_EXISTS_SPAM.append((float)(1+spams_contain_Feature)/(2+self.num_spams))
            # calculate and save Pr(x=0|C=SPAM)
            self.PR_NO_EXISTS_SPAM.append((float)(1+spams_no_contain_Feature)/(2+self.num_spams))
            
        #calculate the HAM probability
        self.PR_HAM = (float)(self.num_hams)/(self.num_hams+self.num_spams)
        
        #calculate the SPAM probability
        self.PR_SPAM = (float)(self.num_spams)/(self.num_hams+self.num_spams)
        
        #open a file(model.txt)
        modelDescriptor = open("model.txt","w")
        
        #IMPORTANT!!! To write a float number to a file first convert it to a string using str() . Also , when writing something to a file always use flush(), otherwise all the characters stay in a buffer in memory till we close the file
        
        #write the HAM probability and the SPAM probability separated by tab
        line = str(self.PR_HAM) + "\t" + str(self.PR_SPAM) + "\n"
        modelDescriptor.write(line)
        modelDescriptor.flush()
        #write the probabilities of every feature to the file 
        for i in range(0, len(self.features)):
            line = str(self.PR_EXISTS_HAM[i])+"\t"+str(self.PR_NO_EXISTS_HAM[i])+"\t"+str(self.PR_EXISTS_SPAM[i])+"\t"+str(self.PR_NO_EXISTS_SPAM[i])+"\n"
            modelDescriptor.write(line)
            modelDescriptor.flush()
        #close file
        modelDescriptor.close()
        print "Classifier's model is computed!!!"
        
    """classify the given email , by using the model"""
    def classify(self,givenEmail):
        #load the features if self.features is empty
        if len(self.features) == 0:
            self.loadFeatures()
            print "features are loaded"
        #load the model if the variables at __init__() are empty
        if len(self.PR_EXISTS_HAM)==0  and len(self.PR_NO_EXISTS_HAM)==0 and len(self.PR_EXISTS_SPAM)==0 and len(self.PR_NO_EXISTS_SPAM)==0 :
            #open model.txt
            model_fileDescr = open("model.txt","r")
            #read first line
            firstLine = model_fileDescr.readline()
            #split
            values = firstLine.split()
            #fill probabilities
            self.PR_HAM = float(values[0])
            self.PR_SPAM = float(values[1])
            
            #now read the other lines
            otherLines = model_fileDescr.readlines()
            #for all lines
            for line in otherLines:
                #split the current line
                otherValues = line.split()
                #fill probabilities
                pr_exists_ham = float(otherValues[0])
                pr_no_exists_ham = float(otherValues[1])
                pr_exists_spam = float(otherValues[2])
                pr_no_exists_spam = float(otherValues[3])

                self.PR_EXISTS_HAM.append(pr_exists_ham)
                self.PR_NO_EXISTS_HAM.append(pr_no_exists_ham)
                self.PR_EXISTS_SPAM.append(pr_exists_spam)
                self.PR_NO_EXISTS_SPAM.append(pr_no_exists_spam)
            model_fileDescr.close()            
            print "model is loaded"
            
        #all the above lines are necessary to load the model if our lists are empty
        
        #now classify the givenEmail
        
        #transform givenEmail to a vector
        givenEmail.setFeatureVector(self.getFeatures())
        givenEmailVector = givenEmail.getEmailVector()
        
        # calculate spam score for givenEmail
        # calculate enumerator PS = P(C=SPAM)*P(X|C=SPAM)
        tmp = 1
        #for every index(i) in the vector(use index-based for-loop)
        for i in range(0, len(givenEmailVector)):
        # if vector[i] is 1 then multiply temporary float with PR_EXISTS_SPAM[i]
            if givenEmailVector[i] == 1:
                tmp = tmp * self.PR_EXISTS_SPAM[i]
            # else multiply temporary float with PR_NO_EXISTS_SPAM[i]
            else:
                tmp = tmp * self.PR_NO_EXISTS_SPAM[i]
        PS = self.PR_SPAM*tmp
        #calculate PH = P(C=HAM)*P(X|C=HAM)
        tmp = 1
        #for every index(i) in the vector(use index-based for-loop)
        for i in range(0, len(givenEmailVector)):
            # if vector[i] is 1 then multiply temporary float with PR_EXISTS_HAM[i]
            if givenEmailVector[i] == 1:
                tmp = tmp * self.PR_EXISTS_HAM[i]
            # else multiply temporary float with PR_NO_EXISTS_HAM[i]
            else:
                tmp = tmp * self.PR_NO_EXISTS_HAM[i]   
        PH = self.PR_HAM*tmp
        
        score = PS/(PS+PH)
        
        if score > 0.5:
            return "SPAM"
        else:
            return "HAM"
