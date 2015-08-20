#!/usr/bin/env python

"""
exciseRepeats.py

Author: Tony Papenfuss
Date: Fri Mar 21 13:25:51 EST 2008

"""

import os, sys, re
from mungo.fasta import FastaFile


iFilename = sys.argv[1]
oFilename = iFilename + '.excised'

# Cleaned & now masked reads
fi = FastaFile(iFilename)
fo = FastaFile(oFilename, 'w')
for h,s in fi:
    s = s.replace('N', '')
    fo.write(h,s)
fi.close()
fo.close()
