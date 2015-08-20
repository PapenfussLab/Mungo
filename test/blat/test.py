#!/usr/bin/env python

"""
test.py

Author: Tony Papenfuss
Date: Tue Aug  5 10:50:04 EST 2008

"""

import os, sys
from blat import BlatFile


f = BlatFile('results_0000000.txt', multi=True)
for chain in f.iterBestHits():
    print chain
    print
