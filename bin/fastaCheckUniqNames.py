#!/usr/bin/env python

"""
fastaCheckUniqNames.py

Author: Tony Papenfuss
Date: Mon May 14 10:37:47 EST 2007

"""

import sys
from optparse import OptionParser
from mungo.fasta import FastaFile


usage = "%prog <input fasta file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args(sys.argv[1:])

if '-' in args:
    faFile = FastaFile(sys.stdin)
else:
    faFile = FastaFile(args[0])

headers = {}
for h,s in faFile:
    tokens = h.split()
    name = tokens[0]
    try:
        headers[name].append(h)
    except KeyError:
        headers[name] = [h]

for name in headers:
    if len(headers[name])>1:
        print 'Non-unique fasta ids:'
        for h in headers[name]:
            print h
        print
        print

         