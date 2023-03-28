# Session 9 - Using BERT-style models for Cultural Data Science

## Overview

In the previous weeks, we've looked at some quite technical things in class, like language modelling and how to build RNNs using ```TensorFlow```. In today's lecture, we were introduced to some of the basic features underlying the so-called *transformer architecture* and specfically the model called BERT.

BERT is used to create *contextual embeddings* - word embeddings which take into account the fact that the same token in different contexts might have different meanings. These contextual embeddings allow us to do some interesting things with our data, which we're looking into today. 

In the code along session, we're going to work with [BERTopic](https://maartengr.github.io/BERTopic/index.html), a really fun and easy to use package for doing *topic modelling* with BERT-style contextual embeddings. What we're doing with topic modelling is trying to find particular clusters or patterns in the data which correspond to something like topics or themes. Earlier approaches to LDA were widely used but completely unsuited for this task - BERTopic does not have the same limitations. 

For this session, we'll be working with an exploratory notebook made by the creator of BERTopic. You can access this either via [Colab](https://colab.research.google.com/drive/1FieRA9fLdkQEGDIMYl0I3MCjSUKVF8C-?usp=sharing) or on UCloud.

## Tasks

- Discussing topic modelling
- Describing BERTopic
- Thinking about results
- Experimenting, tinkering, playing!
