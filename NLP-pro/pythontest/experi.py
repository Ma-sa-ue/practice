__author__ = 'masatoshi'
__author__ = 'masatoshi'

import csv
import numpy as np
import prepre
import yomikomi2
from nltk.stem import PorterStemmer
from gensim import corpora, models, similarities



file_name ='hey.csv'
file_name ='qqq2.csv'
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

f.close()
j=1394
with open("experi.txt","w") as f:
        i = aaa[-1500+j-1]
        print i
        print yomikomi2.func_dic3(55)
        print yomikomi2.func_dic3(143)
        print yomikomi2.func_dic3(42)
        print yomikomi2.func_dic3(46)
        print yomikomi2.func_dic3(46)
        ###print yomikomi2.func_dic3(97)
        f.write(i)
        f.write("\n")
        f.write("\n")
print 5