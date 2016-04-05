import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.WARNING)

from gensim import corpora, models, similarities, utils
from nltk.corpus import stopwords
import os, pickle, nltk
import numpy as np
# os.chdir('/Users/rbnsnsd2/Documents/Python/LSA')

#Load the documents from the .csv pre-processing step .csv -> documents
documents = pickle.load( open("gooddreads.pkl", "rb"))
ratings = pickle.load( open("gooddreads_rating.pkl", "rb"))

# remove common words and tokenize
stoplist = nltk.corpus.stopwords.words('english')
texts = [[word for word in utils.simple_preprocess(document) if word not in stoplist]for document in documents]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]
         for text in texts]

def preprocessing_stop(document, stoplist):
    texts = [word for word in utils.simple_preprocess(document) if word not in stoplist]
    return texts

#Create a dictionary for the texts
dictionary = corpora.Dictionary(texts)
# dictionary.save('review.dict') #Save the dictionary

#Transform the texts into a bow corpus representation
corpus = [dictionary.doc2bow(text) for text in texts]
# corpora.MmCorpus.serialize('review.mm', corpus) #Save the bow corpus

#Transform the bow corpus into tfidf weighted corpus
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

nm = 300
# print('number of topics:',nm)
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=nm, power_iters=4) # initialize LSI transformation
corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
index = similarities.MatrixSimilarity(corpus_lsi) #Create an index based on the bow->ifidf->lsi corpus
#index.save('LSA_goodreads.index')

#Create a cosine similarity array of all documents
simmatrix = []
for sims in index:
    simmatrix.append(sims)
SimMatrix = np.array(simmatrix).reshape(-1,len(simmatrix))

def QSim(document): #Query function for document d
    doc_processed = preprocessing_stop(document, stoplist)
    vec_bow = dictionary.doc2bow(doc_processed)
    vec_lsi = lsi[tfidf[vec_bow]] # convert the query to LSI space
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return sims[:5]

def MSim(document): #Query function to find index of max value
    doc_processed = preprocessing_stop(document, stoplist)
    vec_bow = dictionary.doc2bow(doc_processed)
    vec_lsi = lsi[tfidf[vec_bow]] # convert the query to LSI space
    sims = index[vec_lsi]
    return np.argmax(sims)

AP = 0
for i in range(len(documents)):
    if i < 10:
        print QSim(documents[i])
    if ratings[i] == ratings[MSim(documents[i])]:
        AP = AP + 1
    else:
        print i, MSim(documents[i])

print 'Rating accuracy:', AP/float(len(documents))
print lsi.projection.s