#!/usr/bin/env python

"""
fastaCountMajor.py <filename> <length cutoff>
"""

import sys
from mungo.fasta import *

filename = sys.argv[1]
cutoff = int(sys.argv[2])

count = 0
for h,s in FastaFile(filename):
    if len(s)>=cutoff:
        count += 1
print count
