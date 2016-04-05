import numpy

import pyximport
pyximport.install(inplace=True, setup_args={"include_dirs": numpy.get_include()})

# import test_sdot

import word2vec
import itertools

sentences = list(itertools.islice(word2vec.Text8Corpus('/Users/kofola/workspace/word2vec/text8'), 100))
model = word2vec.Word2Vec(sentences[:1], size=10, min_count=0)
print model.syn0
