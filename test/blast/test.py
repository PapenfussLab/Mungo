#!/usr/bin/env python

"""
test.py

Author: Tony Papenfuss
Date: Fri Aug 22 13:02:05 EST 2008

"""

import os, sys
from blast import *


data = []
for b in BlastFile('data.txt'):
    data.append(b)

print 'Raw'
for b in data:
    print b
print

print 'Strands'
for b in data:
    print b.strand()
print
