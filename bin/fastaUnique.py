#!/usr/bin/env python

"""
fastaUnique.py <input file> <output file>

Author: Tony Papenfuss
Date: Wed Apr  2 09:53:14 EST 2008

"""

import os, sys
from mungo.fasta import FastaFile

from optparse import OptionParser
usage = "%prog <Input file1> <Output file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
parser.add_option('-i', '--stdin', dest='stdin', action='store_true', help='Input from stdin')
parser.add_option('-o', '--stdout', dest='stdout', action='store_true', help='Output to stdout')
options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()

if options.stdin:
    f = FastaFile(sys.stdin)
else:
    f = FastaFile(args[0])

if options.stdout:
    w = FastaFile(sys.stdout, 'w')
else:
    w = FastaFile(args[1], 'w')

accList= []
for h,s in f:
    acc = h.split()[0]
    if not acc in accList:
        w.write(h,s)
        accList.append(acc)
w.close()
f.close()
