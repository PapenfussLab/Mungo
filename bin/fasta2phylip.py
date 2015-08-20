#!/usr/bin/env python

"""
clustal2phylip.py <input filename> <output filename>

Author: Tony Papenfuss
Date: Mon Jan  8 11:44:37 EST 2007

"""

import os, sys
from optparse import OptionParser
from mungo.align import Alignment


usage = "%prog [options] <input file> <output file>"
parser = OptionParser(usage=usage)
options, args = parser.parse_args(sys.argv)

if len(args)!=3:
    sys.exit(__doc__)

iFilename = args[1]
oFilename = args[2]

alignment = Alignment.load(iFilename, format='fasta')
alignment.save(oFilename, format='phylip')
