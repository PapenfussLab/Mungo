#!/usr/bin/env python

"""
fasta_average_length.py

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


for filename in args:
    n = 0
    average = 0L
    for h,s in FastaFile(filename):
        n += 1
        average += len(s)
    print '%s\t%i' % (filename, float(average)/n)
