import nltk
from nltk.book import *

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max()

bigrams = nltk.bigrams(text3)
cfd = nltk.ConditionalFreqDist(bigrams)

print cfd['living']
generate_model(cfd, 'living')
