#!/usr/bin/env python

"""
fastaRename.py <iFilename> <oFilename>

Author: Tony Papenfuss
Date: Fri Mar  7 14:17:14 EST 2008

"""

import sys
from mungo.fasta import FastaFile


iFilename = sys.argv[1]
oFilename = sys.argv[2]


def getSpp(line):
    token = line.split('[')[-1].split(']')[0]
    return token


writer= FastaFile(oFilename, 'w')
for h,s in FastaFile(iFilename):
    tokens = h.split()
    name = tokens[0]
    spp = getSpp(h)
    sppParts = spp.split()
    h2 = "%s%s_%s" % (sppParts[0][0:5], sppParts[1][0:2].title(), name)
    writer.write(h2, s)
writer.close()
