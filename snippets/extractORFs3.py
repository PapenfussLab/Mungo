#!/usr/bin/env python

"""
extractORFs.py

Author: Tony Papenfuss
Date: Wed Aug 23 08:52:58 EST 2006

"""

import os, sys
import re, copy
import fasta, sequence, hmmer3
from hmmer3 import hmmer2frame


pattern = re.compile('[\*|X{200,}]')
minLen = 20

i = 0
writer = fasta.MfaWriter('ORFs.fa')
faFile = fasta.load_iter('6frames.fa')

for header,seq in faFile:
    header = header.strip()
    print >> sys.stderr, header
    block,hmmerFrame = header.split(':')
    frame = hmmer2frame[int(hmmerFrame)]
    
    matchIter = pattern.finditer(seq)
    try:
        match = matchIter.next()
    except StopIteration:
        print match
        print seq
        sys.exit()
    start = match.start()
    for match in matchIter:
        end = match.start()
        orf = seq[start+1:end]
        length = len(orf)
        if length>=minLen:
            i += 1
            chrom,bStart,bEnd,gStart,gEnd,strand = \
                hmmer3.convertBlock6FrameToGenomic(header,start+1,end+1)
            h = '%s.%i.%i-%i  length %i' % (block,i,gStart,gEnd,length)
            writer.write(h, orf)
        start = copy.copy(end)
writer.close()
