import nltk
from nltk.book import *
from nltk.corpus import stopwords

def top50words(text,st):
    td = {}
    for word in text:
        if word in st:
            continue
        if False == td.has_key(word):
            td[word] = 1
        else:
            td[word] += 1
    
    tw = sorted(td.items(), key=lambda(k,v):v, reverse=True)
    tw = tw[:50]
    res = []
    for word, count in tw:
        res.append(word)
    return res

def top50bigrams(text, st):
    td = {}
    symbols = [',',' ','.','?','!']
    for i in range(0,len(text)-1):
        if text[i] in st or text[i] in symbols:
            continue
        if text[i+1] in st or text[i+1] in symbols:
            i = i+1
            continue
        key = text[i] + " " + text[i+1]
        if False == td.has_key(key):
            td[key] = 1
        else:
            td[key] += 1
    
    tb = sorted(td.items(), key=lambda(k,v):v, reverse=True)
    tb = tb[:50]
    res = []
    for word, count in tb:
        res.append(word)
    return res

st = stopwords.words('english')
print top50words(text1, st)
print top50bigrams(text1, st)
