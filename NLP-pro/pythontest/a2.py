__author__ = 'masatoshi'

import csv
import numpy as np
import prepre
from nltk.stem import PorterStemmer
from gensim import corpora, models, similarities



file_name ='hey.csv'
file_name ='qqq2.csv'
aaa=[]
yyy1=[]
yyy2=[]

lmtzr = PorterStemmer()
### read data from hey.csv
count =0
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    ###header = next(reader)
    for row in reader:
        aaa.append(row[0])
        count += 1
        if(count==10000):
            break

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

g = open("new_doc2","w")
for i in texts:
    g.write(" ".join(i)+"\n")
g.close()
