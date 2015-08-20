#!/usr/bin/env python

"""
reverse_comp.py <filename>

Prints the reverse complement of a DNA string (in Fasta format).
"""

import sys

import Fasta
import Sequence


if len(sys.argv)!=2 or '-h' in sys.argv or '--help' in sys.argv:
    sys.exit(__doc__)

iFilename = sys.argv[1]
header, seq = Fasta.load(iFilename)

seq = Sequence.reverse_complement(seq.upper())

print '>%s' % header
for i in xrange(0, len(seq), 80):
    print seq[i:i+80]
