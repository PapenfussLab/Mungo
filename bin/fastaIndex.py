#!/usr/bin/env python

"""
fastaIndex.py <fasta file>

Author: Tony Papenfuss
Date: Wed Apr 23 14:49:40 EST 2008

"""

import os, sys
from mungo.fasta import FastaFile


if len(sys.argv)==1 or '-h' in sys.argv:
    sys.exit(__doc__)

iFilename = sys.argv[1]
f = FastaFile(iFilename, indexed=True)
