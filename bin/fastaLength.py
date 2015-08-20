#!/usr/bin/env python

"""
fastaLength.py

Author: Tony Papenfuss
Date: Wed Mar 26 14:59:54 EST 2008
"""

import sys
from optparse import OptionParser
import mungo.fasta as fasta
from mungo.fasta import FastaFile


usage = "%prog [-s|--stdin] <input filename>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
parser.add_option('-s', '--stdin', action='store_true', dest='stdin',
    help='Take input from stdin')
options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()


if options.stdin:
    faFile = FastaFile(sys.stdin)
else:
    faFile = FastaFile(args[0])

for h,s in faFile:
    print h, len(s)
