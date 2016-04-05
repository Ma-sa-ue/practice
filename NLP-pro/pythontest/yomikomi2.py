__author__ = 'masatoshi'

import csv

dict={}
dict2 ={}
dict3 ={}
stop = ['Life Sciences & Biomedicine','Physical Sciences','Technology','Arts & Humanities','Social Sciences']

def convert_big(i):
    if(i<=74):
        return 1
    elif(i<=91):
        return 2
    elif(i<=112):
        return 3
    elif(i<=126):
        return 4
    else:
        return 5

with open('category.txt','r') as f:
    i=0
    for line in f.readlines():
        line = line.strip()
        if(line!='' and line not in stop):
            dict.update({line:i})
            dict3.update({i:line})
            dict2.update({line:convert_big(i)})
            i = i+1
dict.update({"Audiology & Speech-Language Pathology":151})
dict2.update({"Audiology & Speech-Language Pathology":3})

dict.update({"Science & Technology - Other Topics":152})
dict.update({"Life Sciences & Biomedicine - Other Topics":153})
dict.update({'Arts & Humanities - Other Topics':154})
dict.update({'Social Sciences - Other Topics':155})

f.close()
###print dict["Virology"]
###print dict["Research & Experimental Medicine"]


def func_dic(x):
    return dict[x]

def func_dic2(x):
    return dict2[x]

def func_dic3(x):
    return dict3[x]
print dict.keys()

ccc =[]
counter =0
__author__ = 'masatoshi'
import csv

my_key=[]

for i in range(5000/500):
    j = (i+1)*500
    j = str(j)
    my_key.append((6-len(j))*'0'+j)

second_key=[str(2000+i) for i in range(0,12)]

###print my_key

ddd =[]
for my_key_j in second_key:
    for my_key_i in my_key:
        print my_key_i,my_key_j
        if((my_key_i=='004000' and my_key_j=='2010')!=1 and (my_key_i=='003500' and my_key_j=='2002')!=1 and (my_key_i=='3500' and my_key_j=='002000')!=1 and (my_key_i=='002000' and my_key_j=='2008')!=1 ):
            with open('./utokyo_1900_2015/'+my_key_j+'_'+my_key_i+'.tsv', 'r') as f:
                    reader = csv.reader(f,delimiter = '\t')
                    header = next(reader)
                    for row in reader:
                        if(row[21]!=""):
                            row_pesdo = row[-5].strip()
                            kkk = row_pesdo.split('; ')
                            for i in kkk:
                                if(i not in dict.keys()):
                                    dict.update({i:156+counter})
                                    counter+=1
                            if(len(kkk)!=0  and  "Other Topics" not in kkk[0] and ''not in kkk):
                                ccc.append([row[21],map(func_dic,kkk),[func_dic2(kkk[0])]])
                                ddd.append([map(func_dic,kkk),[func_dic2(kkk[0])],row[32],row[9]])
            f.close()

with open('todai.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(ccc)
with open('todai_pesdo.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(ddd)
f.close()

print len(dict.keys())
print len(ccc)
