import nltk
from nltk.corpus import brown

def word_freq(word, genre):
    word_list = brown.words(categories=genre)
    num = 0
    for w in word_list:
        if w == word:
            num += 1
    return num

print word_freq('result', 'news')

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

genres = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
cfd.tabulate(conditions=genres, samples=modals)
