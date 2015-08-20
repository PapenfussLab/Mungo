#!/usr/bin/env python

"""
fastaSlice.py <fasta file> <first entry> <number>

Author: Tony Papenfuss
Date: Wed Apr 23 14:49:40 EST 2008

"""

import os, sys
from mungo.fasta import FastaFile


if len(sys.argv)==1 or '-h' in sys.argv:
    sys.exit(__doc__)

iFilename = sys.argv[1]
start = int(sys.argv[2])
n = int(sys.argv[3])

f = FastaFile(iFilename, indexed=True)
f.seek(start)

w = FastaFile(sys.stdout, 'w')
count = 0
for h,s in f:
    w.write(h,s)
    count += 1
    if count==n: break
