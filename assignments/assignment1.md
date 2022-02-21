# Assignment 1 - Collocation tool

In the previous lesson, we saw that words which frequently co-occur together in a given context are known as _collocates_. We also saw that we could calculate the _strength of association_ between collocates, allowing us to see how much two words are related to one another. This is important because of the _distributional hypothesis_ - that you can learn a lot about what a word means based on the other words that appear around it.

For this assignment, you will write a small Python program to perform collocational analysis using the string processing and NLP tools you've already encountered. Your script should do the following:

- Take a user-defined search term and a user-defined window size.
- Take one specific text which the user can define.
- Find all the context words which appear ± the window size from the search term in that text.
- Calculate the mutual information score for each context word.
- Save the results as a CSV file with (at least) the following columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score.

For this assignment, you should create a private Github repository and add me as a collaborator. When submitting via Brightspace, simply send the link to the repository; I will provide feedback and comments via Github's built in functionality.

## Tips and pointers
- You are welcome to work on this and submit as a group, even though it says Individual Assignment.
- Try to provide a README file which outlines the contents of the repository.
- For your dataset, you should use the novels in the shared data folder, under _100 English Novels_. **You should not include the data in your Github repo - an empty folder called data is fine**
- Calculate mutual information using **either** the score we looked at in class **or** the formula outlined on the website for the [British National Corpus]("https://www.english-corpora.org/mutualInformation.asp"). The latter approach here is a little easier, I think, and totally acceptable to use.
- Be sure to pay attention to tokenization, capital letters, punctuation, etc. All of these could affect your final scores!

## Bonus tasks
- Create a program which does the above for every novel in the corpus, saving one output CSV per novel
- Create a program which does this for the whole dataset, creating a CSV with one set of results, showing the mutual information scores for collocates across the whole set of texts
- Create a program which allows a user to define a number of different collocates at the same time, rather than only one

## Goals and outcomes
- The goal of this assignment is to demonstrate that you have a good understanding of how to use simple text processing techniques to extract valuable information from text data
- Essentially we are attemping to replicate the kind of functionality available in the online web interfaces that we saw last week but on a dataset of our choosing
- After completing this assignment, you will have a simple collocation tool which can in principal be resused on another text dataset of your choice