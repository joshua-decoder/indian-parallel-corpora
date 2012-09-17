#!/usr/bin/env python

# Generates the document splits for each language pair.  After running this script, you will find
# directories of the form
#
#   PAIR/doc/TYPE.DOCID.LANG[.NUM]
#
# where
#
#   PAIR is the language pair (e.g., "ur-en")
#   TYPE is the data split (dev, devtest, test, and train)
#   DOCID is the document ID
#   LANG is the language (e.g., "ur", "en")
#   NUM is the reference number (0, 1, 2, or 3, for English only)


from collections import defaultdict
import sys
import os
from itertools import *

def write_files(segs,type):

    def filewriter(file):
        return open(file, 'w')

    for docno in segs.keys():
        outfiles = map(filewriter,
                       [os.path.join(pair,"doc",'%s.doc-%s.%s' % (type, docno, lang)),
                        os.path.join(pair,"doc",'%s.doc-%s.en.0' % (type, docno)),
                        os.path.join(pair,"doc",'%s.doc-%s.en.1' % (type, docno)),
                        os.path.join(pair,"doc",'%s.doc-%s.en.2' % (type, docno)),
                        os.path.join(pair,"doc",'%s.doc-%s.en.3' % (type, docno))])

        sentnos = map(int,sorted(segs[docno], key=lambda x: int(x)))
        for i in range(max(sentnos) + 1):
            sentno = `i`
            if (segs[docno].has_key(sentno)):
                tup = segs[docno][sentno]
            else:
                tup = tuple(['\n' for n in range(5)])
            for j in range(len(tup)):
                outfiles[j].write(tup[j])
                
for lang in ['bn', 'hi', 'ml', 'ta', 'te', 'ur']:
    pair = lang + '-en'

    if not os.path.exists(os.path.join(pair, 'doc')):
        os.mkdir(os.path.join(pair, 'doc'))

    for type in ['training']:
        segs = {}

        files = [os.path.join(pair,'%s.%s.seg_ids' % (type, pair)),
                 os.path.join(pair,'%s.%s.%s' % (type, pair, lang)),
                 os.path.join(pair,'%s.%s.en' % (type, pair))]

        for segid,fr,en in zip(*map(open, files)):
            segid = segid.rstrip()
            docno, sentno = segid.split('_')
            
            if not segs.has_key(docno):
                segs[docno] = dict()

            if not segs[docno].has_key(sentno):
                segs[docno][sentno] = [fr]

            segs[docno][sentno].append(en)

        # convert to a tuple, done to fill in missing values in training file
        for docno in segs.keys():
            for sentno in segs[docno].keys():
                list = segs[docno][sentno]
                while len(list) < 5:
                    list.append('\n')

                segs[docno][sentno] = tuple(list)

        write_files(segs,type)


    for type in ['dev', 'devtest', 'test']:
        segs = {}

        files = [os.path.join(pair,'%s.%s.seg_ids' % (type, pair)),
                 os.path.join(pair,'%s.%s.%s' % (type, pair, lang)),
                 os.path.join(pair,'%s.%s.en.0' % (type, pair)),
                 os.path.join(pair,'%s.%s.en.1' % (type, pair)),
                 os.path.join(pair,'%s.%s.en.2' % (type, pair)),
                 os.path.join(pair,'%s.%s.en.3' % (type, pair))]

        for segid,fr,en0,en1,en2,en3 in zip(*map(open, files)):
            segid = segid.rstrip()
            docno, sentno = segid.split('_')
            
            if not segs.has_key(docno):
                segs[docno] = dict()
            segs[docno][sentno] = (fr, en0, en1, en2, en3)

        write_files(segs,type)


