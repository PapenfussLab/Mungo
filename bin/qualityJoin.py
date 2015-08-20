#!/usr/bin/env python

"""
qualityJoin.py <Input file1> [<Input file2> ...] <Output file>

Author: Tony Papenfuss
Date: Thu Mar  6 11:18:10 EST 2008

"""

import sys
import glob
from quality import QualityFile

iFilenames = sys.argv[1:-1]
oFilename = sys.argv[-1]

writer = QualityFile(oFilename, 'w')
for iFilename in iFilenames:
    print '%s-->%s' % (iFilename, oFilename)
    f = QualityFile(iFilename)
    for h,s in f:
        writer.write(h,s)
    f.close()
    writer.flush()
writer.close()
