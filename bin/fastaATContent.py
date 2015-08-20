#!/usr/bin/env python

"""
calcATContent.py

Author: Tony Papenfuss
Date: Wed Jul  8 10:18:32 EST 2009

"""

import os, sys
from mungo.fasta import FastaReader


iFilename = sys.argv[1]

nAT = 0
total = 0
for h,s in FastaReader(iFilename):
    nAT += s.count("A") + s.count("T")
    total += len(s)
print "AT content %0.2f" % (100.0*nAT/total)
