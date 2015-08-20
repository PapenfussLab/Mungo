#!/usr/bin/env python

"""
doBlast.py

Author: Tony Papenfuss
Date: Fri Oct 20 12:26:08 EST 2006

"""

import os, sys, glob
from useful import extractRootName


cmd = 'blast -p tblastn -d %s -i %s -o %s'
blastdb = '/database/opossum/assembly/blastdb/assembly'

filenames = glob.glob('seq/*')
for filename in filenames:
    name = extractRootName(filename)
    print name
    oFilename = 'blast/%s.txt' % name
    os.system(cmd % (blastdb, filename, oFilename))
