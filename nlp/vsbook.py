import nltk
from nltk.book import *

def lexical_diversity(text):
    return len(text) / len(set(text))

len1 = len(text1)
len2 = len(text2)
words1 = len(set(text1))
words2 = len(set(text2))
awl1 = sum([len(word) for word in text1])/len1
awl2 = sum([len(word) for word in text2])/len2
ld1 = len1/words1
ld2 = len2/words2

print "text length:", len1, len2
print "words count:", words1, words2
print "averge word length:", awl1, awl2
print "lexical diversity:", ld1, ld2
