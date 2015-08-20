#!/usr/bin/env python

"""
extractSeq.py [options] <fasta file> <start> <end>
"""

import sys
from optparse import OptionParser

import fasta
import sequence


usage = "%prog [options] <fasta file> <start> <end>"
parser = OptionParser(usage=usage)
# parser.add_option(
#     "-o", "--output", 
#     dest="oFilename",
#     help="Output filename", 
#     default=None)
parser.add_option(
    "-w", "--width", 
    dest="width",
    type="int",
    help="Output sequence width (Default: 60)", 
    default=60)
parser.add_option(
    "-r", "--rev", "--reverse",
    action="store_true",
    dest="reverse",
    help="Reverse sequence", 
    default=False)
parser.add_option(
    "-c", "--comp", "--complement",
    action="store_true",
    dest="complement",
    help="Complement sequence", 
    default=False)
parser.add_option(
    "-b", "--reverseComplement", "--revComp",
    action="store_true",
    dest="reverseComplement",
    help="Reverse complement sequence", default=False)
options, args = parser.parse_args(sys.argv)

iFilename = args[1]
start = int(args[2])
end = int(args[3])

header,seq = fasta.load(iFilename)
s = seq[start-1:end]

h = '%s %i-%i' % (header,start,end)
if options.reverse:
    s = sequence.reverse(s)
    h += '(r)'
elif options.complement:
    s = sequence.complement(s)
    h += '(c)'
elif options.reverseComplement:
    s = sequence.reverse_complement(s)
    h += '(rc)'

fasta.pretty(h, s, width=options.width)
