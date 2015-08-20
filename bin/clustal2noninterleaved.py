#!/usr/bin/env python

"""
clustal2noninterleaved.py <input file> <output file>

Author: Tony Papenfuss
Date: Fri May 11 23:33:06 EST 2007

"""

import os, sys
from optparse import OptionParser
from mungo.align import Alignment


usage = "%prog [options] <input file> <output file>"
parser = OptionParser(usage=usage)
options, args = parser.parse_args(sys.argv)

if len(args)!=3:
    sys.exit(__doc__)

aln = Alignment.loadClustal(args[1])
aln.saveClustal(args[2], interleaved=False)
