import nltk
from nltk.corpus import brown

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

genre_word = [(word, genre)
              for genre in ['news','romance']
              for word in brown.words(categories=genre)
              if word in days]

cfd = nltk.ConditionalFreqDist(genre_word)
print cfd.conditions()
print cfd['news']
cfd.tabulate(conditions=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
cfd.plot(cumulative=True)
