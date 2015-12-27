import nltk

names = nltk.corpus.names
male_names = names.words('male.txt')
female_names = names.words('female.txt')
common = [w for w in male_names if w in female_names]
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid)
)

cfd.plot()
