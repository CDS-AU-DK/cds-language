# Assignment 3 - Text classification

We've seen in the past few sessions how text classification works, both from the perspective of classical machine learning and from more contemporary deep learning perspectives. In most cases, we've seen how a simple model like a ```LogisticRegression Classifier``` provides a solid benchmark which we can build on using more sophisticated models.

We've also seen that *word embeddings* can be employed to make dense vector representations of words, encoding linguistic information about the word and it's relationship to other words. In class this week, we saw that these word embeddings can be fed into classifiers, potentially improving the performance and generalizability of our classifier models.

The assignment for this week builds on these concepts and techniques. We're going to be working with the data in the folder ```CDS-LANG/toxic``` and trying to see if we can predict whether or not a comment is a certain kind of *toxic speech*. You should write two scripts which do the following:

- The first script should perform benchmark classification using standard machine learning approaches
  - This means ```CountVectorizer()``` or ```TfidfVectorizer()```, ```LogisticRegression``` classifier
  - Save the results from the classification report to a text file
- The second script should perform classification using the kind of deep learning methods we saw in class
  - Keras ```Embedding``` layer, Convolutional Neural Network
  - Save the classification report to a text file 

## Tips and pointers (READ THIS BIT)
- Try to provide a detailed README file which outlines the contents of the repository.
- Create a folder called *in* or *input* or *data*. This should be the folder where data goes, if you were to use the tool again in future.
- Save results in a clearly-named folder like *output*, *out*, or *results*
- **You should not include the data in your Github repo - an empty folder called data is fine**

## Bonus tasks
- Add a range of different ```Argparse``` parameters that would allow the user to interact with the code, such as the embedding dimension size, the CountVector parameters.
  - Think about which parameters are most *likely* to be modified by a user.
  
## Goals and outcomes

- The goal of this assignment is to show that you can perform text classification using *both* classical machine learning approaches, as well as using more sophisticated deep learning approaches
- The scripts that you create for this assignment can also be reused and modified for use on other text data in a tabular format.