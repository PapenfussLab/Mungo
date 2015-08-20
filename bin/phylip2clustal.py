#!/usr/bin/env python

"""
phylip2clustal.py [options] <input file> <output file>

Author: Tony Papenfuss
Date: Tue Jun  5 10:25:24 EST 2007

"""

import os, sys
from optparse import OptionParser
import align


usage = "%prog <input file> <output dir>"
parser = OptionParser(usage=usage, version="%prog - Version 1")

parser.add_option(
    "-n", "--nonInterleaved",
    action="store_true",
    dest="nonInterleaved",
    help="Save sequence in non-interleaved format", default=False)

options, args = parser.parse_args(sys.argv)


iFilename = args[1]
oFilename = args[2]

aln = align.Alignment.load(iFilename, format='phylip')

aln.save(oFilename, format='clustal', interleaved=not options.nonInterleaved)

    