#!/usr/bin/env python

"""
clustal2phylip.py [-w width] <input filename> <output filename>

Author: Tony Papenfuss
Date: Mon Jan  8 11:44:37 EST 2007

"""

import os, sys
from optparse import OptionParser
from mungo.align import Alignment


usage = "%prog [-w width] <input file> <output file>"
parser = OptionParser(usage=usage)
parser.add_option('-w', '--width', dest='width', action='store', 
    type='int', default=10, help='Name field width')
options, args = parser.parse_args(sys.argv)

iFilename = args[1]
oFilename = args[2]

alignment = Alignment.loadClustal(iFilename)
alignment.save(oFilename, format='phylip', width=options.width)
