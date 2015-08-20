#!/usr/bin/env python

"""
fastaCleanup.py < <input file> > <output file>
"""

import sys


def load_mfa_iter(iFile):
    'Returns a multi-fasta file generator'
    header = None
    seq = None
    for line in iFile:
        line = line.strip()
        if line:
            if line[0]=='>':
                if seq:
                    yield header, ''.join(seq)
                header = line[1:]
                seq = []
            else:
                line = ''.join(line.split())
                seq.append(line)
    yield header, ''.join(seq)


if __name__=='__main__':
    faFile = load_mfa_iter(sys.stdin)
    for header,seq in faFile:
        print '>%s' % header
        w = 60
        for i in xrange(0,len(seq),w):
            print seq[i:i+w]
        print
