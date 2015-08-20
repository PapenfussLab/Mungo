#!/usr/bin/env python

"""
translate.py [-] <filename>

Translates a DNA sequence to a protein sequence
"""

import sys
from optparse import OptionParser

from mungo.fasta import FastaFile, pretty
from mungo import sequence


usage = "%prog [options] <fasta file>"
parser = OptionParser(usage=usage)
parser.add_option("-o", "--output", dest="oFilename",
  help="Output filename", default=None)
parser.add_option("-w", "--width", dest="width", type="int",
  help="Sequence width", default=60)

options, args = parser.parse_args(sys.argv)

if len(args)!=2: sys.exit(__doc__)


if args[1]!='-':
    faFile = FastaFile(args[1])
else:
    faFile = FastaFile(sys.stdin)

if options.oFilename:
    oFile = open(options.oFilename, 'w')
else:
    oFile = sys.stdout

for header,seq in faFile:
    protein = sequence.translate(seq)
    print >> oFile, '>%s' % header
    print >> oFile, pretty(protein, width=options.width)
