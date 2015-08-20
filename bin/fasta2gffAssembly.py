#!/usr/bin/env python

"""
fasta2gffAssembly.py <fasta file pattern>

Author: Tony Papenfuss
Date: Mon Feb 25 14:54:57 EST 2008

"""

import os, sys, glob
from mungo.fasta import FastaFile
import mungo.gff as gff


iFilePattern = sys.argv[1]

oFile = open('assembly.gff', 'w')
for filename in glob.iglob(iFilePattern):
    f = FastaFile(filename)
    for h,L in f.lengthGenerator():
        print filename, h, L
        g = gff.Feature()
        g.reference = h
        g.source = 'assembly'
        g.type = 'chrom'
        g.start = 1
        g.end = L
        g.group = 'Reference %s' % h
        oFile.write(str(g) + '\n')
        oFile.flush()
oFile.close()
