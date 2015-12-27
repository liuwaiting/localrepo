import nltk
from nltk.corpus import swadesh

en2ca = swadesh.entries(['en','ca'])
translate = dict(en2ca)
print translate['dog']
