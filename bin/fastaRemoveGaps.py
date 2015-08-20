#!/usr/bin/env python

"""
fastaRemoveGaps.py [-] <input file>
"""

import sys
from optparse import OptionParser
import mungo.old.fasta as fasta
from mungo.useful import *


def main(iFileHandle, oFileHandle):
    iFile = fasta.load_mfa_iter(iFileHandle)
    oFile = smartopen(oFileHandle)
    for h,s in iFile:
        s = s.replace('-','')
        s = s.replace('.','')
        fasta.pretty(h, s, stream=oFile)


if __name__=='__main__':
    usage = "%prog [options] [-] <input file> [> <output file>]"
    parser = OptionParser(usage=usage, version="%prog - Version 1")
    parser.add_option('-o', '--output',
        type="string", dest="output", default=None,
        help="Output file")
    parser.add_option('-s', '--stdin',
        action="store_true", dest="stdin", default=False,
        help="Read from standard input.")
    
    options, args = parser.parse_args(sys.argv)
    
    if options.stdin or '-' in args:
        iFileHandle = sys.stdin
    else:
        iFileHandle = args[-1]
    
    if options.output:
        oFileHandle = option.output
    else:
        oFileHandle = sys.stdout
    
    main(iFileHandle, oFileHandle)
