#!/usr/bin/env python

"""
clustal2fasta.py <input file> <output file>
"""

import sys
from optparse import OptionParser
from mungo.align import Alignment
from mungo.fasta import FastaWriter


usage = "%prog [options] <input file> <output file>"
parser = OptionParser(usage=usage)
options, args = parser.parse_args(sys.argv)

if len(args)!=3:
    sys.exit(__doc__)

aln = Alignment.loadClustal(args[1])
writer = FastaWriter(args[2])
for name in aln:
    writer.write(name, aln[name])
writer.close()
