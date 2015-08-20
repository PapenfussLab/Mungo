#!/usr/bin/env python

"""
reverse_comp.py <filename>

Prints the reverse complement of a DNA string (in fasta format).
"""

import sys
import mungo.fasta as fasta
import mungo.sequence as sequence


if len(sys.argv)!=2 or '-h' in sys.argv or '--help' in sys.argv:
    sys.exit(__doc__)

if sys.argv[1]!='-':
    faFile = fasta.load_iter(sys.argv[1])
else:
    faFile = fasta.load_iter(sys.stdin)

for h,s in faFile:
    rc = sequence.complement(s.upper())
    
    print '>%s' % h
    print fasta.pretty(rc)
