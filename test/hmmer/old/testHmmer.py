#!/usr/bin/env python

"""
testHmmer.py

Author: Tony Papenfuss
Date: Fri Sep  1 09:09:02 EST 2006

"""

import os, sys, re
import hmmer4, fasta, sequence


h,s = fasta.load('seq/HLA-A.fa')
L = len(s)

if False:
    domains = hmmer4.load_domains('hmmer/6frames.txt')
    for d in domains:
        p = hmmer4.parseSixFrameHeader(d.accession)
        print d
        print p.name, p.frame
        gStart,gEnd,strand = hmmer4.convert6FrameToGenomic(d.sStart,d.sEnd,p.frame,L)
        print gStart,gEnd,strand
        if strand=='+':
            dna = s[gStart-1:gEnd]
            print len(dna), len(dna) % 3==0
            print sequence.codons(dna, remainder=True)
            print sequence.translate(dna)
        else:
            gStart,gEnd = gEnd,gStart
            dna = sequence.reverseComplement(s[gStart-1:gEnd])
            print len(dna), len(dna) % 3==0
            print sequence.codons(dna, remainder=True)
            print sequence.translate(dna)
        print
else:
    domains = hmmer4.load_domains('hmmer/ORFs.txt')
    for d in domains:
        o = hmmer4.parseOrfHeader(d.accession)
        print d
        print o
        gStart,gEnd = hmmer4.convertOrfToGenomic(d.sStart,d.sEnd,o.strand,o.start)
        if o.strand=='+':
            dna = s[gStart-1:gEnd]
        else:
            gStart,gEnd = gEnd,gStart
            dna = sequence.reverseComplement(s[gStart-1:gEnd])
        print gStart, gEnd
        print len(dna), len(dna) % 3==0
        print sequence.codons(dna, remainder=True)
        print sequence.translate(dna)
        print
