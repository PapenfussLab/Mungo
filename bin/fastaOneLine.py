#!/usr/bin/env python

"""
fastaOneLine.py [- <] <filename>

Author: Tony Papenfuss
Date: Wed Apr 11 21:41:25 EST 2007

"""

import sys
from optparse import OptionParser
from mungo.fasta import FastaFile


if len(sys.argv)==1: sys.exit(__doc__)

usage = "%prog [- <] <input fasta file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")

options, args = parser.parse_args(sys.argv)

if '-' in args:
    iFile = sys.stdin
else:
    iFile = open(sys.argv[-1])

for header,seq in FastaFile(iFile):
    print '>%s' % header
    print seq
    print
