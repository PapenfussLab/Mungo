#!/usr/bin/env python

"""
extractORFs.py

Author: Tony Papenfuss
Date: Wed Aug 23 08:52:58 EST 2006

"""

import os, sys
import re, copy
import fasta, sequence, hmmer3


seqFilename = sys.argv[1]

header,seq = fasta.load(seqFilename)
header = header.split()[0]
L = len(seq)

pattern = re.compile('\*')
minLen = 10

sixFrameIter = sequence.sixFrameTranslationIter(seq)

writer = fasta.MfaWriter(sys.stdout)
i = 0
for frame,p in sixFrameIter:
    print >> sys.stderr, 'Frame:', frame
    
    matchIter = pattern.finditer(p)
    match = matchIter.next()
    start = match.start()
    for match in matchIter:
        end = match.start()
        orf = p[start+1:end]
        length = len(orf)
        if length>=minLen:
            gStart,gEnd,strand = hmmer3.convertSixFrameToGenomic(start+1, end+1, frame, L)
            
            i += 1
            h = '%s.%i.%i-%i  length %i' % (header, i, gStart, gEnd, length)
            writer.write(h, orf + '\n')
            
        start = copy.copy(end)
writer.close()
