#!/usr/bin/env python

"""
reverse_comp.py <filename>

Prints the reverse complement of a DNA string (in fasta format).
"""

import sys

from mungo import fasta
from mungo import sequence


if len(sys.argv)!=2 or '-h' in sys.argv or '--help' in sys.argv:
    sys.exit(__doc__)

for h,s in fasta.FastaFile(sys.argv[1]):
    rc = sequence.reverseComplement(s.upper())
    
    print '>%s' % h
    print fasta.pretty(rc)
