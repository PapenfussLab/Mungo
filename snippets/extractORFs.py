#!/usr/bin/env python

"""
extractORFs.py

Author: Tony Papenfuss
Date: Wed Aug 23 08:52:58 EST 2006

"""

import os, sys
import re, copy
import fasta, sequence, hmmer


def Initialize():
    header,seq = fasta.load('MHC_hg18.fa')
    sixFrameIter = sequence.sixFrameTranslationIter(seq)
    writer = fasta.MfaWriter('6frames.fa')
    for frame,p in sixFrameIter:
        print 'Frame:', frame
        writer.write('%s:%i' % (header,frame),p)
    writer.close()
    sys.exit()


# Initialize()

header,seq = fasta.load('MHC_hg18.fa')
L = len(seq)
hstart = header.split()[0]

pattern = re.compile('\*|X{200,}')
minLen = 20

# sixFrameIter = sequence.sixFrameTranslationIter(seq)
sixFrameIter = fasta.load_iter('6frames.fa')

writer = fasta.MfaWriter('ORFs.fa')
i = 0
for h,p in sixFrameIter:
    hmmerFrame = int(h.split(':')[-1])
    frame = hmmer.hmmer2frame[hmmerFrame]
    print >> sys.stderr, 'Frame:', frame
    if frame>0:
        strand = '+'
    else:
        strand = '-'
    
    matchIter = pattern.finditer(p)
    match = matchIter.next()
    start = match.start()
    for match in matchIter:
        end = match.start()
        orf = p[start+1:end]
        length = len(orf)
        if length>=minLen:
            gStart,gEnd = hmmer.convertSixFrameToGenomic(start+2, end, frame, L)
            
            i += 1
            h = '%s.%i.%i-%i  length %i' % (hstart, i, gStart, gEnd, length)
            writer.write(h, orf + '\n')
            
#             if strand=='+':
#                 print orf
#                 print [x for x in sequence.codonIterator(seq[gStart-1:gEnd], remainder=True)]
#                 print sequence.translate(seq[gStart-1:gEnd])
#             else:
#                 start,end = gEnd,gStart
#                 print orf
#                 print [x for x in sequence.codonIterator(sequence.reverseComplement(seq[start-1:end]), remainder=True)]
#                 print sequence.translate(sequence.reverseComplement(seq[start-1:end]))
#             print
        start = copy.copy(end)
writer.close()
