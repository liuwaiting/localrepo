import nltk
from nltk.corpus import wordnet as wn

print wn.synsets('motorcar')
#car.n.01 => car,noun,first sense
#motorcar belongs to the first noun sense of car
print wn.synset('car.n.01').lemma_names()
#[u'car', u'auto', u'automobile', u'machine', u'motorcar']
#a collection of synonymous words (lemmas)
print wn.synset('car.n.01').definition()
print wn.synset('car.n.01').examples()

#hyponyms:a word of more specific meaning than a general or superordinate term applicable to it. 
motorcar = wn.synset('car.n.01')
#get a collection of hyponyms of motorcar
types_of_motorcar = motorcar.hyponyms()
allhy = sorted([lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()])
print allhy

#hypernyms:a word with a broad meaning that more specific words fall under a superordinate.
hyper = motorcar.hypernyms()
paths = motorcar.hypernym_paths()
print len(paths)#there are 2 paths
path1 = [synset.name() for synset in paths[0]]
path2 = [synset.name() for synset in paths[1]]
print "path1:",path1
print "path2:",path2
print motorcar.root_hypernyms()

#More Lexical Relations
#meronyms:a term that denotes part of something but which is used to refer to the whole of it
#holonyms:the thins they are contained in
#three relations: part, substance, member

print wn.synset('tree.n.01').part_meronyms()
#burl, crown, stump, trunk, limb is part of tree
print wn.synset('tree.n.01').substance_meronyms()
#heartwood and sapwood is substance of tree
print wn.synset('forest.n.01').member_meronyms()
#the member of forest is tree

print wn.synset('trunk.n.01').part_holonyms()
#tree
print wn.synset('heartwood.n.01').substance_holonyms()
#tree
print wn.synset('tree.n.01').member_holonyms()
#forest

for synset in wn.synsets('mint', wn.NOUN):
    print synset.name() + ':', synset.definition()

#batch.n.02: (often followed by `of') a large number or amount or extent
#mint.n.02: any north temperate plant of the genus Mentha with aromatic leaves and small mauve flowers
#mint.n.03: any member of the mint family of plants
#mint.n.04: the leaves of a mint plant used fresh or candied
#mint.n.05: a candy that is flavored with a mint oil
#mint.n.06: a plant where money is coined by authority of the government

print wn.synset('eat.v.01').entailments()
#eat entails swallow and chew
print wn.lemma('supply.n.02.supply').antonyms()
#supply vs demand
