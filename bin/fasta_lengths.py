#!/usr/bin/env python

"""
fastaLengths.py

Author: Tony Papenfuss
Date: Wed Mar 26 15:03:28 EST 2008
"""

import sys
from mungo.fasta import FastaFile
from optparse import OptionParser


usage = "%prog <Input file1> [<Input file2> ...]"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()


total = 0L
for filename in args:
    for h,s in FastaFile(filename):
        name = h.split()[0]
        L = len(s)
        total += L
        print '%s\t%s\t%i' % (filename, name, L)

