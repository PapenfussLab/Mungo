#!/usr/bin/env python

"""
6frameToGenome.py <hmmer file>

@author: Tony Papenfuss
@since: Mon Jul  3 14:14:13 EST 2006

"""

import os, sys
import hmmer


iFilename = sys.argv[1]

domains = hmmer.load_domains(iFilename, seqType=hmmer.BlockSixFrameDomain)
for d in domains:
    d.toGenomic()
    print d
