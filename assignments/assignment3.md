# Assignment 3 - Network analysis

In the last few classes, we've seen lots of different ways to extract quantatitive information from text data. This includes things like: distribution of grammatical features; sentiment scores; named entities; collocations; and so on. Last week, we also saw how we can use network analysis as a _formalism_ which allows us to describe objects by their relations. 

In this assignment, you are going to write a ```.py``` script which can be used for network analysis. As we saw last week, pretty much anything can be formalised as a network. We're not going to focus on creating the edgelists for this project; instead, the goal is to have a script that would work the same way on _any_ input data, as long as the input format is correct. 

So, as test data, I recommend that you use the files in the folder called ```network_data```. However, the final script should be able to be resused and work on any undirected, weighted edgelist with the same column names.

Your script should do the following:

- If the user enters a _single filename_ as an argument on the command line:
  - Load that edgelist
  - Perform network analysis using ```networkx```
  - Save a simple visualisation
  - Save a CSV which shows the following for every node:
    - name; degree; betweenness centrality; eigenvector_centrality
- If the user enters a _directory name_ as an argument on the command line:
  - Do all of the above steps for every edgelist in the directory
  - Save a separate visualisation and CSV for each file

## Tips and pointers (READ THIS BIT)
- Be careful to check the delimiter in the test data! (tab delimited)
- You are welcome to work on this and submit as a group, even though it says Individual Assignment.
- Try to provide a detailed README file which outlines the contents of the repository.
- Create a folder called *in* or *input* or *data*. This should be the folder where data goes, if you were to use the tool again in future.
- Save results in a clearly-named folder like *output*, *out*, or *results*
- **You should not include the data in your Github repo - an empty folder called data is fine**

## Bonus tasks

- ```networkx``` offers a range of different plotting algorithms. Select a few of these and all the user to decide between different options.

## Goals and outcomes

- The goal of this assignment is to demonstrate that you have a good understanding of how to perform network analysis on undirected, weighted edgelists using ```networkx```.
- By the end of this assignment, you will have a script which can be resued for future projects to perform a quick, simple network analysis 