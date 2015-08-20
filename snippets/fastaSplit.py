#!/usr/bin/env python

"""
fastaSplit.py <fasta file> <output dir>
"""

import sys
import Fasta


if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv)==1:
    sys.exit(__doc__)

Fasta.split(sys.argv[1], oDir=sys.argv[2])
