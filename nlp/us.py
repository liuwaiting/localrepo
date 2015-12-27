import nltk
from nltk.corpus import state_union

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ['men','women','people']
    if w.lower() == target
)

cfd.tabulate()
cfd.plot()

