#!/usr/bin/env python

"""
gff2fasta.py [OPTIONS] <gff file> <fasta reference sequence>

Options:

"""

import sys
from optparse import OptionParser

import gff
import fasta
import sequence

usage = "%prog [options] <gff file> <fasta reference sequence>"
parser = OptionParser(usage=usage)
parser.add_option("-o", "--output", dest="oFilename",
  help="Output filename", default=None)
parser.add_option("-f", "--features", dest="features",
  help="Features to extract", default=['exon'])
options, args = parser.parse_args(sys.argv)

if len(args)!=3:
    sys.exit(__doc__)

gffFilename = args[1]
faFilename = args[2]

data = gff.load(gffFilename)
header,seq = fasta.load(faFilename)

if options.oFilename:
    oFile = open(options.oFilename, 'w')
else:
    oFile = sys.stdout

writer = fasta.MfaWriter(oFile)
for name in data:
    s = []
    extrema = []
    for f in data[name]:
        if f.type in options.features:
            if f.strand=='+':
                start,end = f.start,f.end
                _seq = seq[start-1:end]
            else:    
                start,end = f.start,f.end
                _seq = seq[start-1:end]
                _seq = sequence.reverse_complement(_seq)
            s.append(_seq)
            extrema.append(f.start)
            extrema.append(f.end)
    start = min(extrema)
    end = max(extrema)
    if f.strand=='-':
        s.reverse()
    s = ''.join(s)
    h = 'gene_%s %s:%s-%s(%s)' % (f.extractName(),f.reference,start,end,f.strand)
    writer.write(h, s)
writer.close()
