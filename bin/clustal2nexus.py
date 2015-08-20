#!/usr/bin/env python

"""
clustal2nexus.py <input file> <output file>
"""

import sys
from optparse import OptionParser
from mungo.align import Alignment


usage = "%prog [options] <input file> <output file>"
parser = OptionParser(usage=usage)
options, args = parser.parse_args(sys.argv)

if len(args)!=3:
    sys.exit(__doc__)

aln = Alignment.load(args[1], format='clustal')
aln.save(args[2], format='nexus')
