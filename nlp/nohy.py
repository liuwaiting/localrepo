import nltk
from nltk.corpus import wordnet as wn

all_syn = wn.all_synsets('n')

none_syn = 0
total = 0
for syn in all_syn:
    total += 1
    if len(syn.hyponyms()) == 0:
        none_syn += 1

percent = none_syn*1.0/total
print percent
