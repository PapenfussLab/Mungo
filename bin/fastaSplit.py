#!/usr/bin/env python

"""
fastaSplit.py <fasta file> <output dir>
"""

import sys
from optparse import OptionParser
from mungo.fasta import *


usage = "%prog <input file> <output dir>"
parser = OptionParser(usage=usage, version="%prog - Version 1")

options, args = parser.parse_args(sys.argv)

if len(args)!=3:
    sys.exit(__doc__)


reader = FastaFile(args[1])
for h,s in reader:
    acc = h.split()[0]
    writer = FastaFile(os.path.join(args[2], acc + ".fa"), "w")
    writer.write(h,s)

