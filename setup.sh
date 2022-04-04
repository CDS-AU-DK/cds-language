#!/usr/bin/env bash

pip install --upgrade pip
pip install spacy tqdm spacytextblob vaderSentiment networkx scikit-learn tensorflow gensim
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md