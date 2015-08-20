#!/usr/bin/env python

"""
makeFastaIndex.py <fasta file>

Author: Tony Papenfuss
Date: Wed Feb 20 14:45:30 EST 2008

"""

import sys
import fasta
from useful import smartopen


if __name__=='__main__':
    iFilename = sys.argv[1]
    index = fasta.FastaIndexFactory(iFilename)
