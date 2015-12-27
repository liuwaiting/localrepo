import nltk
from nltk.corpus import wordnet as wn

def supergloss(s):
    res = s.definition()
    for hyper in s.hypernyms():
        res += ";" + hyper.definition()
    for hypo in s.hyponyms():
        res += ";" + hypo.definition()
    return res

print supergloss(wn.lemma('car.n.01.automobile').synset())

