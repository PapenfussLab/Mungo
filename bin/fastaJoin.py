#!/usr/bin/env python

"""
fastaJoin.py <Input file1> [<Input file2> ...] <Output file>

Author: Tony Papenfuss
Date: Thu Mar  6 11:18:10 EST 2008

"""

import sys
import glob
from mungo.fasta import FastaFile

from optparse import OptionParser
usage = "%prog <Input file1> [<Input file2> ...] <Output file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()

iFilenames = args[:-1]
oFilename = args[-1]

writer = FastaFile(oFilename, 'w')
for iFilename in iFilenames:
    print >> sys.stderr, '%s-->%s' % (iFilename, oFilename)
    f = FastaFile(iFilename)
    for h,s in f:
        writer.write(h,s)
    f.close()
    writer.flush()
writer.close()
