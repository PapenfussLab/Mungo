#!/usr/bin/env python

"""
clustalRenameFromIndex.py <iFilename> <oFilename> [<index filename> default=index.txt]

Author: Tony Papenfuss
Date: Fri Mar  7 14:17:14 EST 2008

"""

import sys
import mungo.align as align


iFilename = sys.argv[1]
oFilename = sys.argv[2]
if len(sys.argv)==4:
    idxFilename = sys.argv[3]
else:
    idxFilename = 'index.txt'


aln = align.Alignment.loadClustal(iFilename)

index = {}
for line in open(idxFilename):
    tokens = line.strip().split('\t')
    index[tokens[0]] = (tokens[1], tokens[2])

for name in aln:
    origName, spp = index[name]
    sppParts = spp.split()
    newName = "%s%s_%s" % (sppParts[0][0:5], sppParts[1][0:2].title(), origName)
    aln.rename(name, newName)

aln.saveClustal(oFilename)
