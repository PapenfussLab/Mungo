#!/usr/bin/env python

"""
convertDelimiter.py <input>

Author: Tony Papenfuss
Date: Tue Jun 10 16:53:54 EST 2008

"""

import os, sys, tempfile


iFilename = sys.argv[1]
delimiter = '|'
newDelimiter = '\t'

fd,name = tempfile.mkstemp()
for line in open(iFilename):
    tokens = line.strip().split(delimiter)
    print >> fd, newDelimiter.join(tokens)
fd.close()
os.rename(name, iFilename)
