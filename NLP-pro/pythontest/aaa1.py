from gensim import corpora, models, similarities
import numpy as np
import scipy as sp

corpus = corpora.MmCorpus('deerwester.mm')
dictionary = corpora.Dictionary.load('deerwester.dict')

corpus_sci = scipy.mmread('deerwester.mm')
tfidf = models.TfidfModel(corpus)
corpus =list(corpus)

bag_of =[]
for doc in corpus[0:1000]:
    bag_of.append(doc)

true_bag_of = []
kkkk = len(dictionary.token2id)

'''
### to see the keys
print dictionary.token2id
'''
for i in bag_of:

    p = np.zeros(kkkk)
    for j in i:
        p[j[0]] = j[1]
    true_bag_of.append(p)
k=0
for q in true_bag_of[0]:
	if(q!=0):
		k=k+1
print k
print np.shape(true_bag_of)

