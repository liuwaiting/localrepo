import nltk
from nltk.corpus import brown

table = {}
for genre in brown.categories():
    table[genre] = []
    words = len(brown.words(categories=genre))
    table[genre].append(words)
    types = len(set(brown.words(categories=genre)))
    table[genre].append(types)
    divers = words*1.0/types
    table[genre].append(divers)

print 'genre','words','type','diversity'
for genre, num in table.items():
    print genre,num[0],num[1],num[2]
