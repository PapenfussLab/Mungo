#!/usr/bin/env python

"""
fasta_block_split.py <iFilenames> <oFilename>

Author: Tony Papenfuss
Date: Fri Mar 30 12:58:58 EST 2007

"""

import os, sys
from mungo.fasta import FastaFile

from optparse import OptionParser
usage = "%prog [-b <block_size>] <input_file1> [<input_file2> ...] <output_file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
parser.add_option("-b", "--blocksize", action="store", type="int", 
    dest="blocksize", default="10000000")

options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()


iFilenames = args[:-1]
oFilename = args[-1]

writer = FastaFile(oFilename, 'w', blockSize=10000000)
for iFilename in iFilenames:
    for h,s in FastaFile(iFilename):
        writer.write(h,s)
writer.close()
