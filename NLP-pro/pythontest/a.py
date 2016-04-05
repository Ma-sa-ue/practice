__author__ = 'masatoshi'

import csv
import numpy as np
import prepre
from nltk.stem import PorterStemmer
from gensim import corpora, models, similarities



file_name ='hey.csv'
file_name ='todai.csv'
aaa=[]
yyy1=[]
yyy2=[]

lmtzr = PorterStemmer()
### read data from hey.csv
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    ###header = next(reader)
    for row in reader:
        aaa.append(row[0])
        yyy1.append(row[1])
        yyy2.append(row[2])

print 5
#######################
### exclude the docuement of no abstract 
#####################
texts=[]

for kkk in range(len(aaa)):
    if(len(aaa[kkk]) ==0):
        print "error"
    texts.append(aaa[kkk])


texts = prepre.preprocess_documents(texts)
for document in texts:
    map(lmtzr.stem,document)


##################

print texts[2]
### make corpus
dictionary = corpora.Dictionary(texts)
dictionary.filter_extremes(no_below=5, no_above=0.1)
dictionary.save('deerwester_todai.dict')
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('deerwester_todai.mm', corpus)


'''
### to make tf_idf_corpus
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
'''
'''
### make bag of words matrix
bag_of =[]
for doc in corpus:
    bag_of.append(doc)

true_bag_of = []
kkkk = len(dictionary.token2id)
'''
'''
### to see the keys
print dictionary.token2id
'''
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
'''