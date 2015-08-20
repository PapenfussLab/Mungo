#!/usr/bin/env python

"""
fastaOneCharPerLine.py [--stdin] <filename>

Author: Tony Papenfuss
Date: Wed Apr 11 21:41:25 EST 2007

"""

import sys
from optparse import OptionParser
from mungo.fasta import FastaFile


if len(sys.argv)==1: sys.exit(__doc__)

usage = "%prog [- <] <input fasta file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
parser.add_option('-s', '--stdin', action='store_true', dest='stdin')
options, args = parser.parse_args()

if options.stdin in args:
    faFile = FastaFile(sys.stdin)
else:
    faFile = FastaFile(args[0])

for header,seq in faFile:
    print '>%s' % header
    for b in seq:
        print b
    print
