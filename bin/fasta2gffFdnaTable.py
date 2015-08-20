#!/usr/bin/env python

"""
fasta2gffFdnaTable.py <input fasta pattern> <output sql dump file>

Author: Tony Papenfuss
Date: Mon Jun 16 22:48:07 EST 2008

"""

import os, sys, glob
from mungo.fasta import FastaFile


iFilePattern = sys.argv[1]
oFilename = sys.argv[2]
delimiter = '|'

oFile = open(oFilename, 'w')
for iFilename in glob.iglob(iFilePattern):
    print iFilename
    for h,s in FastaFile(iFilename):
        print h
        name = h.split()[0]
        for i in xrange(0, len(s), 2000):
            print >> oFile, delimiter.join([name, str(i), s[i:i+2000]])
oFile.close()
