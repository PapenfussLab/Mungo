#!/usr/bin/env python

"""
blockify.py <input dir> <output dir>

Author: Tony Papenfuss
Date: Wed Apr 18 19:36:39 EST 2007

"""

import os, sys, glob
from mungo import fasta


def blockify(iFilename, oFilename, blockSize=5000000):
    writer = fasta.FastaWriter(oFilename)
    for h,s in fasta.FastaReader(iFilename):
        h = h.split()[0]
        for start in xrange(0,len(s),blockSize):
            end = min(start+blockSize, len(s))
            header = '%s.%i-%i' % (h, start+1, end)
            writer.write(header, s[start:end])


if __name__=='__main__':
    if len(sys.argv)==1:
        print __doc__
        sys.exit()
    
    iDir = sys.argv[1]
    oDir = sys.argv[2]
    
    iFilenames = glob.glob('%s/*.fa' % iDir)
    # os.chdir(oDir)
    
    for iFilename in iFilenames:
        print iFilename
        oFilename = os.path.join(oDir, os.path.split(iFilename)[-1])
        blockify(iFilename, oFilename)
