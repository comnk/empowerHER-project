import pandas as pd
import spacy
from keyword_spacy import KeywordExtractor

# https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c
# spacy

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("keyword_extractor", last=True, config={"top_n": 20, "min_ngram": 3, "max_ngram": 3, "strict": True, "top_n_sent": 3})

def extract_sample_keywords(scholarid):
    with open('./paper-text/papers-' + scholarid + '.txt', 'r') as file:
        text = file.read().replace('\n', '')
    if text.rstrip() == '': # empty
        return ''
    kws = []
    doc = nlp(text)
    for kw in doc._.keywords:
        kws.append(kw[0])
    return kws

if __name__ == "__main__": 
    tags = extract_sample_keywords("_af8suQAAAAJ")
    print(tags)