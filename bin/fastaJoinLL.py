#!/usr/bin/env python

"""
fastaJoin.py <Input file1> [<Input file2> ...] <Output file>

Author: Tony Papenfuss
Date: Thu Mar  6 11:18:10 EST 2008

"""

import sys
import glob


from optparse import OptionParser
usage = "%prog <Input file1> [<Input file2> ...] <Output file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()


iFilenames = args[:-1]
oFilename = args[-1]

oFile = open(oFilename, 'w')
for iFilename in iFilenames:
    print >> sys.stderr, '%s-->%s' % (iFilename, oFilename)
    iFile = open(iFilename)
    for line in iFile:
        oFile.write(line)
    iFile.close()
    oFile.flush()
oFile.close()
