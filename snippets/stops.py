#!/usr/bin/env python

"""
stops.py

Author: Tony Papenfuss
Date: Mon Apr 17 19:04:42 EST 2006

"""

import os, sys
import sequence


stops = ['TAA','TGA','TAG','taa','tga','tag']
for stop in stops:
    print stop, sequence.reverseComplement(stop)
    