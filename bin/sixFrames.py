#!/usr/bin/env python

"""
translateSixFrames.py [-] <filename>

Translates a DNA sequence in six frames
"""

import sys
from optparse import OptionParser

from mungo import fasta
from mungo import sequence


usage = "%prog [options] <fasta file>"
parser = OptionParser(usage=usage)
parser.add_option("-o", "--output", dest="oFilename",
  help="Output filename", default=None)
parser.add_option("-w", "--width", dest="width", type="int",
  help="Sequence width", default=60)
options, args = parser.parse_args(sys.argv)

if len(args)!=2:
    sys.exit(__doc__)

iFilename = args[1]
if args[1]!='-':
    faFile = fasta.FastaFile(args[1])
else:
    faFile = fasta.FastaFile(sys.stdin)
    
if options.oFilename:
    oFile = open(oFilename, 'w')
else:
    oFile = sys.stdout

for header,seq in faFile:
    h = header.split()[0]
    proteinIter = sequence.sixFrameTranslationIter(seq)
    for frame,protein in proteinIter:
        print >> oFile, '>%s:%i' % (h, frame)
        print >> oFile, fasta.pretty(protein, width=options.width)
