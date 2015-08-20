#!/usr/bin/env python

"""
fastaBuildIndex.py

Author: Tony Papenfuss
Date: Wed May 28 23:47:04 EST 2008

"""

import os, sys
from mungo.fasta import FastaIndexFile


f = FastaIndexFile(sys.argv[1])
f.build(clobber=False)
