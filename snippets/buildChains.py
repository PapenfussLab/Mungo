#!/usr/bin/env python

"""
buildChains0.py

Author: Tony Papenfuss
Date: Wed Sep 20 17:17:35 EST 2006

"""

import os, sys, glob
import blast, chaining


filenames = glob.glob('blast/*.txt')
for filename in filenames:
    hsps = blast.Blast(filename)
    hsps.convertBlockToGenomeCoords()
    chain = chaining.chainWithBestHit(hsps, hsps.bestHit())
    for hsp in chain:
        print hsp
    print '//'
