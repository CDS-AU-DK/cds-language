#!/usr/bin/env bash

pip install --upgrade pip
pip install spacy tqdm vaderSentiment
python -m spacy download en_core_web_sm