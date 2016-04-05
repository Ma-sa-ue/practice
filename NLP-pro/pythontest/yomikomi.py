__author__ = 'masatoshi'
import csv

aaa =[]
my_key=[]

for i in range(50000/500):
    j = (i+1)*500
    j = str(j)
    my_key.append((6-len(j))*'0'+j)

print my_key
for my_key_i in my_key:
    with open('./Newest100000_Japan_wos/2015_'+my_key_i+'.tsv', 'r') as f:
        reader = csv.reader(f,delimiter = '\t')
        header = next(reader)
        for row in reader:
            aaa.append([row[21]])


####bbb=[[i[21]] for i in aaa]

with open('qqq.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(aaa)





