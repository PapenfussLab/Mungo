#!/usr/bin/env python

"""
extractORFs.py <6 frame translation>

Author: Tony Papenfuss
Date: Wed Aug 23 08:52:58 EST 2006

"""

import os, sys
import re, copy
import fasta, sequence


pattern = re.compile('[\*|X{200,}]')
minLen = 20

i = 0
writer = fasta.MfaWriter('ORFs.fa')

filename = sys.argv[1]
header,dna = fasta.load(filename)
header = header.strip()

orfIter = sequence.extractOrfsIter(dna, minLen=minLen, pattern=pattern)
for i,gStart,gEnd,orf in orfIter:
    h = '%s.%i.%i-%i  Length=%i' % (header,i,gStart,gEnd,len(orf))
    writer.write(h, orf)
    
    fasta.pretty(h, orf)
    
    if gStart<gEnd:
        s = dna[gStart-1:gEnd]
        print gStart, gEnd, len(s), len(s) % 3==0
        print sequence.codons(s, remainder=True)
        print sequence.translate(s)
    else:
        gStart,gEnd = gEnd,gStart
        s = dna[gStart-1:gEnd]
        s = sequence.reverseComplement(s)
        print gStart, gEnd, len(s), len(s) % 3==0
        print sequence.codons(s, remainder=True)
        print sequence.translate(s)
        
    print
writer.close()
