#!/usr/bin/env python

"""
orfTest.py

Author: Tony Papenfuss
Date: Tue Aug 22 20:14:57 EST 2006

"""

import os, sys
import fasta, sequence


header,seq = fasta.load('NKC.fa')
orfIterator = fasta.load_iter('ORFs.fa')
writer = fasta.MfaWriter('ORFs2.fa')

for h,orf in orfIterator:
    chrom,block,orfId,limits = h.split()[0].split('.')
    start,end = limits.split('-')
    start = int(start)
    end = int(end)
    
    if start>end:
        strand = '-'
        start,end = end,start
        s = sequence.translate(sequence.reverseComplement(seq[start-1:end]))
    else:
        strand = '+'
        s = sequence.translate(seq[start-1:end])
    
    if s!=orf: print h
    
    writer.write(h,s + '\n')
writer.close()
