#!/usr/bin/env python

"""
fastaRenameToIndex.py <input file> <output file> [<index file> default=index.txt]

Author: Tony Papenfuss
Date: Fri Mar  7 13:32:40 EST 2008

"""

import sys
import re
import mungo.fasta as fasta


iFilename = sys.argv[1]
oFilename = sys.argv[2]
if len(sys.argv)==4:
    idxFilename = sys.argv[3]
else:
    idxFilename = 'index.txt'


freader = fasta.FastaFile(iFilename)
fwriter = fasta.FastaFile(oFilename, 'w')
oFile = open(idxFilename, 'w')

def getSpp(line):
    token = line.split('[')[-1].split(']')[0]
    return token

# prog = re.compile('\[[\w., ]*\]')
format = '%i\t%s\t%s\n'

i = 0
for h,s in freader:
    i += 1
    h2 = str(i)
    fwriter.write(h2, s)
    
    tokens = h.split()
    name = tokens[0]
    # spp = prog.findall(h)[-1][1:-1]
    spp = getSpp(h)
    oFile.write(format % (i, name, spp))

freader.close()
fwriter.close()
oFile.close()

