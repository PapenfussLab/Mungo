#!/usr/bin/env python

"""
testMutation.py

Author: Tony Papenfuss
Date: Wed May 28 10:21:29 EST 2008

"""

import os, sys
from fasta import *


f = FastaFile('HSP100.fa')
h,s = f.readOne()
print h,s
s = s[0:45]

w = FastaWriter('test.fa')
w.write(h,s)

w.setBlockSize(10)
w.write(h,s)
