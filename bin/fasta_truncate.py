#!/usr/bin/env python

"""
fasta_truncate.py

Author: Tony Papenfuss
Date: July 2013

"""

import sys
import argparse
from mungo.fasta import FastaFile


usage = "%prog <length> <Input file> <Output file>"

parser = argparse.ArgumentParser(description='Truncate fasta files')
parser.add_argument('length', type=int, help='Truncate to length')
parser.add_argument('input_filename', type=str, help='Input filename')
parser.add_argument('output_filename', type=str, help='Output filename')
args = parser.parse_args()

w = FastaFile(args.output_filename, 'w')
for h,s in FastaFile(args.input_filename):
    w.write(h, s[0:args.length])
w.close()
