#!/usr/bin/env python

"""
fastq2fasta.py <input fastq file> <fasta file> <quality file>

Author: Tony Papenfuss
Date: Mon Aug 11 13:56:04 EST 2008

"""

import os, sys, copy

from optparse import OptionParser
usage = "%prog <Input file> <fasta file> <quality file>"
parser = OptionParser(usage=usage, version="%prog - Version 1")
options, args = parser.parse_args()
if len(args)==0:
    parser.print_help()
    sys.exit()


iFilename = args[0]
faFilename = args[1]
qFilename = args[2]


class States:
    S = 's'
    Q = 'q'

faFile = open(faFilename, 'w')
qFile = open(qFilename, 'w')

state = States.Q
Ls = -1
Lq = -1
for line in open(iFilename):
    line_s = line.strip()
    if state==States.Q and line[0]=='@' and Lq==Ls:
        state = States.S
        Ls = 0
        Lq = -1
        header = copy.copy(line[1:])
        faFile.write('>%s' % header)
    elif state==States.S and line[0]=='+':
        state = States.Q
        Lq = 0
        qFile.write('>%s' % header)
    else:
        if state==States.S:
            faFile.write(line)
            Ls += len(line_s)
        elif state==States.Q:
            qFile.write(line)
            Lq += len(line_s)
    
    if state==States.Q and Lq>Ls:
        sys.exit('PROBLEM')

faFile.close()
qFile.close()
