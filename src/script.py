"""
An example script processing a single string using spaCy
"""

# load packages
import spacy
#initialize spaCy
nlp = spacy.load("en_core_web_md")

def main():
    text = "This is a string"
    doc = nlp(text)
    for token in doc:
        print(token.text)
        
if __name__=="__main__":
    main()