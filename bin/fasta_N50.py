#!/usr/bin/env python

"""
fasta_N50.py

Author: Tony Papenfuss
Date: Wed Jul  8 11:53:34 EST 2009

"""

import os, sys
import numpy
from optparse import OptionParser
from mungo.fasta import FastaFile


usage = "%prog <Input file1> [<Input file2> ...]"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()


for filename in args:
    lengths = []
    for h,s in FastaFile(filename):
        lengths.append(len(s))
    lengths.sort()
    
    Lmid = 0.5*sum(lengths)
    cumsum = list(numpy.cumsum(lengths))
    cumsum.append(Lmid)
    cumsum.sort()
    i = cumsum.index(Lmid)
    if i>=1:
        print filename, lengths[i-1]
    else:
        print filename, "NA"
