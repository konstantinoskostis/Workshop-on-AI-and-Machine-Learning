__author__ = 'konstantinos'
#####################################################################################################
#IMPORTANT
#str.lower(your_string) -> converts your string to lower-case
#your_string.replace(old,new) -> replaces old string with new string
#your_string.split() -> removes empty strings and returns a list with non-empry strings
#mylist.append(x) -> adds x to mylist
#myDictionary[key] = value -> adds <key,value> to my dictionary
#sorted_dictionary = sorted(myDictionary.items(),key= lambda t : t[1],reverse=True) -> sorts dictionary by value(from highest to lowest)
###################################### FEATURE SELECTION #############################################

#write a function(call it remove_stopwords)
#that takes as a parameter a string text and replaces stop-words like 'and', 'to','the' with ''
#and returns a string
def remove_stopwords(text):
    toRemove = ["to", "and"]
    for item in toRemove:
        text = text.replace(item, " ")
    return text

#write a function(call it str_toLower)
#that takes as a parameter a string text and converts it to lower case string
#and returns the lower-case string
def str_toLower(text):
    text = str.lower(text)
    return text

#the two emails , D1 and D2
D1 = "Hello George"
D2 = "George said hello to everybody and left"

print "D1 = %s  \nD2 = %s" % (D1,D2)

#call remove_stopwords using D1
D1 = remove_stopwords(D1)
#call remove_stopwords using D2
D2 = remove_stopwords(D2)

print "stop-words are removed"

#call str_toLower using D1
D1 = str_toLower(D1)
#call str_toLower using D2
D2 = str_toLower(D2)

print "converted to lower-case"

#create a list and store the words of D1 (use the split() to tokenize text)
D1_words = D1.split()
#create a list and store the words of D2
D2_words = D2.split()

#initialize a dictionary(call it wordDictionary) to store every unique word along with its frequency
wordDictionary = {}
#initialize a list(call it allWords) to store every word
allWords = []
#initialize a list to store the features(call it features)
features = []
#write an algorithm to find the frequency of every word
#and store the word and its frequency to the dictionary
D_words = []
D_words.append(D1_words)
D_words.append(D2_words)

for wordList in D_words:
    for w in wordList:
        allWords.append(w)

for w in allWords:
    frequency = 0
    for i in range(0,len(allWords)):
        if w == allWords[i]:
            frequency += 1
    if w not in features:
        wordDictionary[w] = frequency

#sort the dictionary by frequency(from highest to lowest) and store the result to sorted_features
sorted_features = sorted(wordDictionary.items(),key=lambda t : t[1],reverse=True)
#from sorted_features get key and add it to features
for x in sorted_features:
    features.append(x[0])
print "features are selected"
print features
############################### END OF FEATURE SELECTION ########################################

############################### TRANSFORMATION TO FEATURE VECTORS ################################

#write a function (call it transform) , that takes 3 parameters
# a list(the feature vector to be filled with 1 and 0) , a list of words of a document , the list of features
# AND describes the following algorithm:
#transformation algorithm
#iterate over the features , if the current feature exists inside the list of words of the document
#append 1 to its vector else append 0

def transform(vector = [],words = [],theFeatures = []):
    for f in theFeatures:
        if f in words:
            vector.append(1)
            #print "INSIDE"
        else:
            #print "OUTSIDE"
            vector.append(0)

#initialize a list(call it D1_vector) to store the transformed D1
D1_vector = []
#initialize a list(call it D2_vector) to store the transformed D2
D2_vector = []

#now fill D1_vector , call transform
transform(D1_vector,D1_words,features)
#now fill D2_vector , call transform
transform(D2_vector,D2_words,features)

#print the vectors
print "D1 = <",D1_vector,">"
print "D2 = <",D2_vector,">"
############################### END OF TRANSFORMATION TO FEATURE VECTORS ##########################