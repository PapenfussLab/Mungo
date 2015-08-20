#!/usr/bin/env python

"""
clustalFilterColumns.py <input filename> <output filename>

Author: Tony Papenfuss
Date: Fri Mar  7 11:53:58 EST 2008

Filter columns of alignment, removing highly gappy columns and columns with 
lower case letters.
"""

import sys
import mungo.align as align
import mungo.sequence as sequence


iFilename = sys.argv[1]
oFilename = sys.argv[2]


GAP_CUTOFF = 0.25

aln = align.Alignment.loadClustal(iFilename)
aln2 = align.Alignment()
for spp in aln:
    aln2.add(spp, '')
nSeq = float(aln.numberOfSeqs())

ok = []
for i,col in enumerate(aln.column_iter()):
    isLower = any(x.islower() for x in col)
    gapCount = sum(x=='-' for x in col)
    isGappy = (1-gapCount/nSeq)<GAP_CUTOFF
    if not isLower and not isGappy:
        ok.append(i)

for i in ok:
    aln2.addColumn(aln.column(i))

aln2.saveClustal(oFilename)
