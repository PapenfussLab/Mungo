#!/usr/bin/env python

"""
fasta2nexus.py

Author: Tony Papenfuss
Date: Wed May  9 17:23:18 EST 2007

"""

import os, sys
from mungo.align import Alignment


aln = Alignment.load(sys.argv[1], format='fasta')
aln.save(sys.argv[2], format='nexus')
