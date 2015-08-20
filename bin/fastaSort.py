#!/usr/bin/env python

"""
fastaSort.py [- <] <input file>

Author: Tony Papenfuss
Date: Mon May 14 10:42:30 EST 2007

"""

import sys
from optparse import OptionParser
import mungo.fasta as fasta


def try_int(s):
    "Convert to integer if possible."
    try: return int(s)
    except: return s


def natsort_key(s):
    "Used internally to get a tuple by which s is sorted."
    import re
    return map(try_int, re.findall(r'(\d+|\D+)', s))


if len(sys.argv)==1: sys.exit(__doc__)

usage = "%prog [- <] <input fasta file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args(sys.argv)

if args[1]=='-':
    seqs = fasta.FastaFile(sys.stdin).readAll()
else:
    seqs = fasta.FastaFile(args[1]).readAll()

seqs.sort(key=lambda x: natsort_key(x[0]))
for h,s in seqs:
    print '>%s' % h
    print fasta.pretty(s)
    print
