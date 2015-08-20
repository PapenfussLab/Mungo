#!/usr/bin/env python

"""
stockholm2clustal.py <stockholm filename> <clustal filename>

Author: Tony Papenfuss
Date: Sun May  6 13:34 EST 2007

"""

import os, sys
from mungo.align import Alignment


iFilename = sys.argv[1]
oFilename = sys.argv[2]

alignment = Alignment.loadStockholm(iFilename)
for name in alignment:
    alignment[name] = alignment[name].replace('.', '-')
alignment.saveClustal(oFilename)
