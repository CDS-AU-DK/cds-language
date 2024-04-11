# Assignment 4 - Emotion analysis with pretrained language models

Winter is... just finished, actually.

In class this week, we've seen how pretrained language models can be used for a range of tasks. In this assignment, we're going to use these models to perform some computational text analysis of some culturally significant data - scripts from the television show *Game of Thrones*. The scripts have been split into lines, with additional metadata showing who spoke each line, which episode that line comes from, and which season that episode belongs to.

In this assignment, we are going to investigate whether the emotional profile of this show changed over the course of its seven series, and we want to know which characters exhibit the most extreme emotions.

For this assignment, you should write code which does the following:

- Predict emotion scores for all lines in the data
- For each season
    - Plot the distribution of all emotion labels in that season
- For each emotion label
    - Plot the relative frequency of each emotion across all seasons

Finally, your repository should include a writtens summary and interpretation of what you think this analysis might being showing. You do not need to be a media studies expert here - just describe what you see and what that might mean in this context.


## Starter code and data

The data for this assignment can be found in the ```cds-lang-data``` folder on UCloud. The data itself comes from [this website](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons?select=Game_of_Thrones_Script.csv).

For this exercise, I recommend using the pretrained emotion classifier that we worked with in class. You can load this via HuggingFace using the following code:

```python
classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      return_all_scores=True)
```                      

## Objective

This assignment is designed to test that you can:

1. Make use of pretrained language models via HuggingFace;
2. Extract meaningful structured information from unstructured text data;
3. Interpret and contextualize these results from a cultural data science perspective.

## Some notes

- You'll need to make use of many of the tools you've learned this semester. This includes - but is not necessarily limited to - libraries such as ```pandas``` and ```matplotlib```.
- You may need to think about how best to present your numbers. Are raw frequencies the best choice? Average? Relative frequencies? That's up to you.

## Additional comments

Your code should include functions that you have written wherever possible. Try to break your code down into smaller self-contained parts, rather than having it as one long set of instructions.

For this assignment, you should submit your code *only* as ```.py``` script, *not* as Jupyter Notebooks.

Lastly, remember to follow the repo structure which was discussed in class recently. The assignment on GitHub provides a schematic outline of how this should look.