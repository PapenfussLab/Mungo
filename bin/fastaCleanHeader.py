#!/usr/bin/env python

"""
fastaCleanHeader.py <input file>
"""

import sys
from optparse import OptionParser

import mungo.old.fasta as fasta
from mungo.useful import *


usage = "%prog [options] <input file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args(sys.argv)

faFile = fasta.load_mfa_iter(args[1])
for h,s in faFile:
    h = h.split()[0]
    if '|' in h:
        h = h.split('|')[1]
    print '>%s' % h
    print s
