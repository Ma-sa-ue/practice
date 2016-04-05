#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Radim Rehurek <radimrehurek@seznam.cz>


"""
Fill a running server with DML-CZ and NUMDAM data, using Latent Semantic Analysis.

Run with:
    ./index_wiki.py /Users/kofola/workspace/dml/data/numdam/ train # test creating semantic model
    ./index_wiki.py /Users/kofola/workspace/dml/data/numdam/ index # test indexing documents
    ./index_wiki.py /Users/kofola/workspace/dml/data/dmlcz/ query  # test querying the index on the server
"""

from __future__ import with_statement

import logging
import os, sys
import random
import itertools

import gensim.utils


def itertexts(rootdir, suffix):
    """Iterate over DML-CZ formatted documents, yielding (id, plain text) 2-tuple."""
    accepted = 0
    for root, dirs, files in os.walk(rootdir):
        path = os.path.normpath(root)
        if os.path.basename(path).startswith('#') and os.path.exists(os.path.join(path, 'fulltext.txt')):
            accepted += 1
            if accepted % 1000 == 0:
                logging.info("PROGRESS: at article #%i (%s)" % (accepted, root))
            intid = path[1 + path.rfind('#') : ] + suffix
            yield intid, open(os.path.join(path, 'fulltext.txt')).read()
#            if accepted == 10: break


def iterdocs(rootdir, suffix):
    """Iterate over DML-CZ formatted documents, yielding SimilarityDocument objects."""
#    from gensim.similarities.simserver import simple_preprocess
    for intid, text in itertexts(rootdir, suffix):
#        doc = {'id': str(intid), 'tokens': simple_preprocess(text), 'payload': [intid], 'language': 'en', 'category': ''}
        doc = {'id': str(intid), 'text': text, 'payload': [intid], 'language': 'en', 'category': ''}
        yield doc


def test_training(server, docs):
    """Communicate with the server, modifying its indexes."""
    # first, drop the existing index from the server (if any)
    server.drop_index()
    # create a semantic model on the server
    gensim.utils.upload_chunked(server, docs) # upload documents to the server in smaller chunks
    server.train() # train model on uploaded documents


def test_indexing(server, docs):
    """Communicate with the server, modifying its indexes."""
    # index some documents on the server
    gensim.utils.upload_chunked(server, docs) # upload documents to the server in smaller chunks
    server.index() # index the uploaded documents


def test_query_id(server, query):
    """Query the server, using document id."""
    result = server.find_similar(query['id'])


def rand_suffix():
    return hex(random.randint(0, 0xfffffff))[2:]


def test_query_doc(server, query):
    """Query the server, using fulltext (string; id is ignored)."""
    # query by fulltext (id is ignored)
    # ask for the 5 most similar documents, with a minimum similarity score of 0.5
    result = server.find_similar(query, min_score=0.5, max_results=5)
    assert len(result) <= 5
    assert all([sim >= 0.5 for _, sim in result])



if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info("running %s" % ' '.join(sys.argv))

    program = os.path.basename(sys.argv[0])
    # make sure we have enough cmd line parameters
    if len(sys.argv) < 3:
        print globals()["__doc__"] % locals()
        sys.exit(1)
    dirpath = sys.argv[1]

    import Pyro4
    ns = Pyro4.locateNS()
    server = Pyro4.Proxy(ns.lookup('gensim.testserver'))

    suffix = ''
    docs = lambda : iterdocs(dirpath, suffix)
    tstdocs = list(itertools.islice(docs(), 100))
    for what in sys.argv[2:]:
        if what == 'train':
            test_training(server, docs())
        elif what == 'drop':
            server.drop_index(keep_model=True)
        elif what == 'regen':
            suffix = rand_suffix()
        elif what == 'index':
            test_indexing(server, docs())
        elif what == 'opt':
            server.optimize()
        elif what == 'status':
            print server.status()
        elif what == 'query':
            logging.info("start querying by id")
            repeat = 100
            for i in xrange(repeat):
                query = random.choice(tstdocs) # pick a random document to be the query
                test_query_id(server, query)
            logging.info("end querying by id")

            logging.info("start querying by text")
            for i in xrange(repeat):
                query = random.choice(tstdocs) # pick a random document to be the query
                test_query_doc(server, query)
            logging.info("end querying by text")
        elif what == 'mem':
            print server.memdebug()

    logging.info("finished running %s" % program)
