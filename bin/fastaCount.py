#!/usr/bin/env python

"""
fastaCount.py <filename>
"""

import sys
from mungo.fasta import fastaCount

for filename in sys.argv[1:]:
    print '%s: %i' % (filename, fastaCount(filename))