#!/usr/bin/env python

"""
fastaLength.py <input filename>
"""

import sys
import Fasta


if len(sys.argv)==1 or '-h' in sys.argv or '--help' in sys.argv:
    sys.exit(__doc__)

faFile = Fasta.load_mfa_iter(sys.argv[1])

for h,s in faFile:
    print h, len(s)
