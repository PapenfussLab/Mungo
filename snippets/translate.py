#!/usr/bin/env python

"""
translate.py <filename>

Translates a DNA sequence to a protein sequence
"""

import sys

import Fasta
import Sequence


if len(sys.argv)!=2 or '-h' in sys.argv or '--help' in sys.argv:
    sys.exit(__doc__)

w = 60

iFilename = sys.argv[1]
faFile = Fasta.load_mfa_iter(iFilename)
for header,seq in faFile:
    protein = Sequence.translate(seq)

    print '>%s' % header
    for i in xrange(0, len(protein), w):
        print protein[i:i+w]
