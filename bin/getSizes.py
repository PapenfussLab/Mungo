#!/usr/bin/env python

"""
getSizes.py <filename pattern>

Author: Tony Papenfuss
Date: Thu Apr 19 15:19:18 EST 2007

"""

import os, sys, glob
import fasta


def getSizes(filenames):
    for filename in filenames:
        for h,s in fasta.load_iter(filename):
            name = h.split()[0]
            L = len(s)
            print '%s\t%s' % (name,L)


if __name__=='__main__':
    if len(sys.argv)<2:
        print __doc__
        sys.exit()
    
    filenames = sys.argv[1:]
    getSizes(filenames)
