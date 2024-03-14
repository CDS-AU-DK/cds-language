# Assignment 3 - Query expansion with word embeddings

Have you ever wondered which of your favourite pop stars sing most about "love"? I bet you have.

In this assignment, we're going to be working with a corpus of lyrics from 57,650 English-language songs. You can find a link to the dataset [here](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs). It's also available on UCloud.

At the beginning of the semester, we saw how we could search for individual keywords and count how frequently they appear in a text. In this assignment, we're going to do some ```query expansion``` with word embeddings via ```gensim```. This means we choose a target word, find the most similar words to this target keyword, and then search for *all of those words* in our texts. Instead of just looking for the word "love", we'll be looking for this word and other related words - expanding our query to include a wider range of related words. 

You should write a script which does the following:

- Loads the song lyric data
- Downloads/loads a word embedding model via ```gensim``` (see below)
- Takes a given word as an input and finds the most similar words via word embeddings
- Find how many songs for a given artist feature terms from the expanded query
- Calculate the percentage of that artist's songs featuring those terms
- Print and/or save results in an easy-to-understand way
    - For example, "45% of {ARTIST}'s songs contain words related to {SEARCH TERM}"

## Starter coder

For convenience, I recommend using a small, pretrained model from ```gensim``` like the following. However, this is by no means compulsory - feel free to use a different model if you so wish!

```python
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
```

## Objective

This assignment is designed to test that you can:

1. Pre-process texts in sensible ways;
2. Use pretrained word embeddings for query expansion;
3. Create a resusable command line tool for calculating results based on user inputs.

## Some notes

- You'll need to use ```argparse``` in this code, and I'd recommend structuring your repo to also make use of a ```requirements.txt``` file, virtual environments, and bash scripts for automation and reproduction.
- You should decide yourself which arguments you think make most sense. Perhaps this is which artist the script should work with, or which specific query should be expanded - think about how the tool should behave.

## Additional comments

Your code should include functions that you have written wherever possible. Try to break your code down into smaller self-contained parts, rather than having it as one long set of instructions.

For this assignment, you should submit your code *only* as ```.py``` script, *not* as Jupyter Notebooks.

Lastly, you are welcome to edit this README file to contain whatever information you like. Remember - documentation is important.
