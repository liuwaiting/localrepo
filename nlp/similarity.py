import nltk
from nltk.corpus import wordnet as wn

right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')

print right.lowest_common_hypernyms(minke)
hyper = right.hypernyms()
print hyper

paths = right.hypernym_paths()
for path in paths:
    for item in path:
        print item.name(), item.min_depth()

print right.path_similarity(minke)
print right.path_similarity(orca)
print right.path_similarity(tortoise)
print right.path_similarity(novel)
