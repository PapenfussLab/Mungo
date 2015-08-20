#!/usr/bin/env python

"""
fastaExtract.py <fasta file> <accession> <start> <end>

Extract sequence between given start & end coordinates from fasta file.
"""

import sys
from mungo.fasta import FastaFile, pretty

if '-h' in sys.argv:
    sys.exit(__doc__)

iFilename = sys.argv[1]
accession = sys.argv[2]
try:
    start = int(sys.argv[3])
    end = int(sys.argv[4])
except:
    start = None
    end = None

for h,s in FastaFile(iFilename):
    tokens = h.split()
    if tokens[0]==accession:
        print '>%s:%s-%s' % (tokens[0],start,end)
        if start:
            print pretty(s[start-1:end])
        else:
            print pretty(s)
        break
