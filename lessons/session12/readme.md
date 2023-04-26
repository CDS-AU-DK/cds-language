# Session 12 - Generative language models

## Overview

In class today, we were introduced to two of the most significant *generative language models*. These are models which have been trained on huge quantities of natural language data; and which, in some cases, have been further finetuned on specifically designed to solve particular problems.

We were introduced to two different architectures. The first of these was GPT-2/3/3.5/4, which forms the basis of the now infamous *ChatGPT*. The GPT family are decoder-only transformers, meaning they use a similar kind of attention mechanism as, for example BERT. A second kind of architecture is the T5 family, or what are known as Text-to-Text Transformers. Again, the architecture is not hugely different from what we've already seen; the major difference is that T5 frames specfic NLP problems in a particular way.

These generative language models are so succesful that it's possible to use them on our own data and our own tasks without need for additional fine-tuning. In this case, we carefully design our input prompts in such a way as to allow for the best output without additional training. So today in class, we're going to be looking at *prompt engineering for zero-shot learning*.

## Tasks

- A quick overview of FLAN-T5
- Prompt engineering in ```huggingface```
  - Work with ChatGPT for those who want to sign up
- Specific tasks for testing zero-shot learning ability
  - Grammatical analysis
  - NER
  - Classification
  - Text summarization
  - etc, etc.
