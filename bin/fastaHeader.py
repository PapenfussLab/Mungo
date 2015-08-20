#!/usr/bin/env python

"""
fastaHeader.py <fasta file>

Author: Tony Papenfuss
Date: Mon May  7 09:09:27 EST 2007

"""

import os, sys
from mungo.fasta import FastaFile


for h,s in FastaFile(sys.argv[1]):
    print h
