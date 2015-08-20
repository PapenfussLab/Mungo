#!/usr/bin/env python

"""
fastaStats.py <filename>

Author: Tony Papenfuss
Date: Wed Mar 26 10:00:42 EST 2008
"""

import os, sys
import numpy
from mungo.fasta import FastaFile
from optparse import OptionParser


usage = "%prog <Input file1>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()


print "filename Total_nt Min_length Max_length Mean_length Median_length N50 N_reads>270"
for filename in args:
    data = []
    for h,s in FastaFile(filename):
        L = len(s)
        data.append(L)
    
    if len(data)>0:
        data.sort()
        data = numpy.array(data)
        Ltotal = sum(data)
        c = numpy.cumsum(data)
        N50 = data[numpy.where(c>=0.5*Ltotal)[0][0]]
        N75 = data[numpy.where(c>=0.75*Ltotal)[0][0]]
        print filename, len(data), Ltotal, min(data), max(data), numpy.mean(data), numpy.median(data), N50, len(numpy.where(data>270)[0])
    else:
        print filename, 0, 0, 0, 0, 0, 0, 0, 0, 0
