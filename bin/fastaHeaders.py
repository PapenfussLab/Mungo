#!/usr/bin/env python

"""
fastaHeaders.py <fasta files>

Author: Tony Papenfuss
Date: Mon May  7 09:09:27 EST 2007

"""

import os, sys
from mungo.fasta import FastaFile

for filename in sys.argv[1:]:
    for h,s in FastaFile(filename):
        print h
