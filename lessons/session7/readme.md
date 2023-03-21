# Session 7 - Language modelling 1 (RNNs)

## Overview

So far, we've been seen that we can work with language at multiple different levels. Firstly, we can think about language at the level of *texts* or *documents*, which we can study by creating *document representations*; we saw simple ways to do this using a bag-of-words model and TF-IDF weighting. We also saw last week how we can create numerical representations of individual words, so-called *word embeddings*. These allow us to study word meaning and the relationship between individual words.

However, both the document representations we've looked at and word embeddings suffer from the same problem - they are essentially *static* and do not account for the fact that language has *internal structure*. 

Today, we'll be looking at how we can account for this kind of internal structure in language by using a special kind of neural network. This *recurrent neural network* allows us to account for the internal structure of language and to perform what is called *language modelling*.

The notebook we are working through today was not developed by me, but was instead developed by a team of researchers and engineers at Google. You can see it online [here](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/text_classification.ipynb).

## Tasks

- Introducing the notebook
- Working through it
- Flag your problem
  - Write on the board something you'd like to go over again, or in more detail
- Midterm feedback
