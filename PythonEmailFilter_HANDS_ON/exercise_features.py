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
    return text

#write a function(call it str_toLower)
#that takes as a parameter a string text and converts it to lower case string
#and returns the lower-case string
def str_toLower(text):
    return text

#the two emails , D1 and D2
D1 = "Hello George"
D2 = "George said hello to everybody and left"

print "D1 = %s  \nD2 = %s" % (D1,D2)

#call remove_stopwords using D1

#call remove_stopwords using D2

print "stop-words are removed"

#call str_toLower using D1

#call str_toLower using D2

print "converted to lower-case"

#create a list and store the words of D1 (use the split() to tokenize text)

#create a list and store the words of D2

#initialize a dictionary(call it wordDictionary) to store every unique word along with its frequency

#initialize a list(call it allWords) to store every word

#initialize a list to store the features(call it features)

#write an algorithm to find the frequency of every word
#and store the word and its frequency to the dictionary

print "features are selected"
#print the features

############################### END OF FEATURE SELECTION ########################################

############################### TRANSFORMATION TO FEATURE VECTORS ################################

#write a function (call it transform) , that takes 3 parameters
# a list(the feature vector to be filled with 1 and 0) , a list of words of a document , the list of features
# AND describes the following algorithm:
#transformation algorithm
#iterate over the features , if the current feature exists inside the list of words of the document
#append 1 to its vector else append 0

def transform(vector = [],words = [],theFeatures = []):
    pass

#initialize a list(call it D1_vector) to store the transformed D1
D1_vector = []
#initialize a list(call it D2_vector) to store the transformed D2
D2_vector = []

#now fill D1_vector , call transform

#now fill D2_vector , call transform

#print the vectors
print "D1 = <",D1_vector,">"
print "D2 = <",D2_vector,">"
############################### END OF TRANSFORMATION TO FEATURE VECTORS ##########################