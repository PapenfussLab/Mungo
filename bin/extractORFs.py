#!/usr/bin/env python

"""
extractORFs.py <DNA sequence file> [<minLen (default=20)>]

Author: Tony Papenfuss
Date: Wed Aug 23 08:52:58 EST 2006

"""

import os, sys
import re, copy
import mungo.fasta as fasta
import mungo.sequence as sequence


# Arguments
filename = sys.argv[1]
if len(sys.argv)>2:
    minLen = int(sys.argv[2])
else:
    minLen = 20


pattern = re.compile('[\*|X{200,}]')

i = 0
writer = fasta.MfaWriter('ORFs.fa')

header,dna = fasta.load(filename)
header = header.strip()

orfIter = sequence.extractOrfsIter(dna, minLen=minLen, pattern=pattern)
for i,gStart,gEnd,orf in orfIter:
    h = '%s.%i.%i-%i  Length=%i' % (header,i,gStart,gEnd,len(orf))
    writer.write(h, orf)
writer.close()
