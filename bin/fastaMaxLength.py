#!/usr/bin/env python

"""
fastaMaxLength.py

Author: Tony Papenfuss
Date: Wed Jul  8 11:53:34 EST 2009

"""

import os, sys
from mungo.fasta import FastaFile
import numpy


iFilename = sys.argv[1]
maxLength = -1
for h,s in FastaFile(iFilename):
    maxLength = max(maxLength, len(s))
print maxLength

