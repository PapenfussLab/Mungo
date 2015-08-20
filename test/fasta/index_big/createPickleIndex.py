#!/usr/bin/env python

"""
testTextIndex.py

Author: Tony Papenfuss
Date: Thu May 29 11:44:36 EST 2008

"""

import os, sys
from fasta import FastaFile


filename = '/Users/papenfuss/databases/devil/transcriptome/reads/combined.fa'
f = FastaFile(filename, indexed=True, clobber=True, method='pickle')
