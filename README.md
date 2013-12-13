# The AI Workshop

This is a repository created for a Workshop on Artificial Intelligence and Machine Learning organized by Appsterdam and
SciFY. In this repo , there are several files and folders, but first follow these instructions to get setup:

## Setup Instructions

1. Install Java, it is REQUIRED! [Get it from here](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
1. Install the Python programming language version 2.7(2.7.6) [Get it from here](http://python.org/download/)
if you are on linux you have python installed. I think that the source code can be interpreted by python 2.6 but i have not tested it
1. Install PyCharm. An Integrated Development Environment for Python by JetBrains. [Get it from here](http://www.jetbrains.com/pycharm/download/) download the community edition which is free! OR you can download the [eclipse ide](http://www.eclipse.org/downloads/) and use [the PyDev](http://pydev.org/download.html) that gives you a python ide!

> You can also wite code using your favourite text editor and the python interpreter!

A hands-on introduction to python [can be found here](http://www.youtube.com/watch?v=Gp60Qp3GUBU)

> IF YOU HAVE ANY PROBLEM INSTALLING THE TOOLS , REMEMBER: Youtube IS YOUR FRIEND! SO IS THE Google!

## Files Contained in this repository

In the Workshop we will build a Naive Bayes Classifier in order to learn how to distinguish good emails from bad emails!

The working directory for you to work on is `PythonEmailFilter_HANDS_ON/`, in there you will find:

* The `dataset/` folder contains files(emails) that we will use as data to learn from.
* The `test/` folder contains files(emails) that we will use to test our algorithm.
* The `Email.py` models an electronic message.
* The `exercise_features.py` is a two-part exercise to help you see how we can select important features(words) from a collection of data and in the second part we will see how we can transform every example in the collection of data to a vector(a mathematical representation that we will use for statistical processing).
* The `FeatureSelection.py` contains a class that selects the most important words from our collection(words are ranked using Mutual Information-a real number) and then outputs the first 250 words to a features.txt file.
* The `NaiveBayesClassifier.py` file is responsible for training the algorithm and it is also used to categorize(classify) an email as good(HAM) or bad(SPAM).When the training is done a file `models.txt` is outputed. This is what the algorithm has learned.
* The `Train.py` contains the workflow of the training phase of the whole algorithm(read emails->select features->train algorithm)
* Finally the `Filter.py` is the spam filter application. It reads the collection of emails to test and classifies every email as HAM or SPAM and outputs the results to a results.txt

There are also the folder `PythonEmailFilter_completed/` that contains all the completed source code.

The `python_powerpoint/` contains an introduction to python
The `presentation/` folder contains the theory we will learn and the examples we will do during the workshop 

