#!/usr/bin/env python

"""
fastaMajorN50.py

Author: Tony Papenfuss
Date: Wed Jul  8 11:53:34 EST 2009

"""

import os, sys
from mungo.fasta import FastaFile
import numpy


iFilename = sys.argv[1]
if len(sys.argv)==3:
    Lmin = sys.argv[2]
else:
    Lmin = 500

lengths = []
for h,s in FastaFile(iFilename):
    L = len(s)
    if L>Lmin:
        lengths.append(len(s))
lengths.sort()
lengths = numpy.array(lengths)

Lmid = 0.5*sum(lengths)
cumsum = list(numpy.cumsum(lengths))
cumsum.append(Lmid)
cumsum.sort()
i = cumsum.index(Lmid)

print lengths[i-1]
