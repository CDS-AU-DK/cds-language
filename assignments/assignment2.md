# Assignment 2 - Sentiment and NER

We saw this week that an common application of NLP in cultural data is finding what is known as *named entities*. In previous sessions, we also saw some simple ways of calculating a *sentiment score* for a stretch of natural language. These tasks allow us to extract some potentially interesting information from our data - what exactly is being spoken about in a text and what kind of sentiment does the text show?

For this assignment, you will write a small Python program to perform NER and sentiment analysis using the techniques you saw in class. You have the choice of one of two different tasks:

1. Using the corpus of English novels, write some code which does the following tasks

   - For every novel in the corpus
     - ~~Get the sentiment of the first sentence.~~
     - Get the sentiment of the final sentence.
     - Plot the results over time, with one visualisation showing sentiment of opening sentences over time and one of closing sentences over time.
     - Find the 20 most common geopolitical entities mentioned across the whole corpus - plot the result as a bar chart.

**OR**

2. Using the corpus of Fake vs Real news, write some code which does the following

   - Split the data into two datasets - one of Fake news and one of Real news
   - For every headline
     - Get the sentiment scores
     - Find all mentions of geopolitical entites
     - Save a CSV which shows the text ID, the sentiment scores, and column showing all GPEs in that text
   - Find the 20 most common geopolitical entities mentioned across each dataset - plot the results as a bar charts
  
For this assignment, you should create a private Github repository and add me as a collaborator. When submitting via Brightspace, simply send the link to the repository; I will provide feedback and comments via Github's built in functionality.

## Tips and pointers

- You are welcome to work on this and submit as a group, even though it says Individual Assignment.
- For the sentiment analysis, you are welcome to use either the spaCyTextBlob approach *or* the VADER approach.
- Try to provide a detailed README file which outlines the contents of the repository.
- Save results in a clearly-named folder like *output* or *results*
- For your dataset, you should use either the novels in the shared data folder, under *100 English Novels* **or** the *Fake/Real News* dataset. **You should not include the data in your Github repo - an empty folder called data is fine**

## Bonus tasks

- For the novels, you can try to do the first sentence, too - but this is tricky!
- You're welcome to do both tasks, if you want! But this is not required at all.
- Repeat experiments using both sentiment analysis techniques, in order to compare results.

## Goals and outcomes

- The goal of this assignment is to demonstrate that you have a good understanding of how to perform dictionary-based sentiment analysis
- It also demonstrates that you can use off-the-shelf NLP frameworks like spaCy to perform named entity recognition and extraction
- After completing this assignment, you will have the core skills required to perform similar analysis of other text corpora more relevant to your interests
