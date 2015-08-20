#!/usr/bin/env python

"""
fastaCleanup.py [- <] <input file>
"""

import sys
from optparse import OptionParser
from mungo.fasta import FastaFile

width = 60

if len(sys.argv)==1: sys.exit(__doc__)

usage = "%prog [- <] <input fasta file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args(sys.argv)

if args[1]=='-':
    faFile = FastaFile(sys.stdin)
else:
    faFile = FastaFile(args[1])

for header,seq in faFile:
    print '>%s' % header
    seq = ''.join(seq.split())
    for i in xrange(0,len(seq),width):
        print seq[i:i+width]
    print
