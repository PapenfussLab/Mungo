#!/usr/bin/env python

"""
calcATContent.py

Author: Tony Papenfuss
Date: Wed Jul  8 10:18:32 EST 2009

"""

import os, sys
from mungo.fasta import FastaReader


iFilename = sys.argv[1]
oFilename = sys.argv[2]
if len(sys.argv)==4:
    binSize = int(sys.argv[3])
else:
    binSize = 1000


oFile = open(oFilename, "w")
format = "%s\t%i\t%0.2f\n"
for h,s in FastaReader(iFilename):
    accession = h.split()[0]
    for i in xrange(0, len(s), binSize):
        gc = s[i:i+binSize].count("G")+s[i:i+binSize].count("C")
        oFile.write(format % (accession, i+1, 100.0*gc/binSize))
oFile.close()
