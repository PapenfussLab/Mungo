#!/usr/bin/env python

"""
fastaTotalLength.py

Author: Tony Papenfuss
Date: Wed Jun 25 11:13:57 EST 2008

"""

import os, sys
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
    f = FastaFile(filename)
    for h,L in f.lengthGenerator():
        total += L
print total
