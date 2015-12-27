import nltk
entries = nltk.corpus.cmudict.entries()

word_dict = {}

for word, pron in entries:
    if False == word_dict.has_key(word):
        word_dict[word] = 1
    else:
        word_dict[word] += 1

word_list = []
for k, v in word_dict.items():
    word_list.append([k,v])

word_list = sorted(word_list, cmp=lambda x,y : cmp(x[1],y[1]), reverse=True)

hc = 0
for word in word_list:
    if word[1] == word_list[0][1]:
        hc += 1
    else:
        break

print word_list[0][1], hc
