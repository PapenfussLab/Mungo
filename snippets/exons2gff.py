#!/usr/bin/env python

"""
exons2gff.py <exons file> <gff file> <reference> <source>
"""

import re
import csv
import sys

gffFields = [
    'reference',
    'source',
    'type',
    'start',
    'end',
    'score',
    'strand',
    'phase',
    'group'
]

strand = {'>': '+', '<': '-'}


def exons2gff(iFilename, oFilename, reference, source, _type='mRNA', offset=0, grouptype='mRNA'):
    iFile = open(iFilename)
    oFile = open(oFilename, 'w')
    writer = csv.writer(oFile, dialect='excel-tab', doublequote=False)

    # Stuff to remember between lines
    name = None
    direction = None
    cdsStart = None
    cdsEnd = None

    for line in iFile:
        line = line.strip()

        if line=='' or line[0]=='#': # pass
            pass
        elif line[0]=='>' or line[0]=='<': # Start gene
            matches = re.finditer(' ', line)

            i1 = matches.next().start()
            i2 = matches.next().start()
            i3 = matches.next().start()

            direction = line[0:i1]
            start = int(line[i1+1:i2]) + offset
            end = int(line[i2+1:i3]) + offset
            name = line[i3+1:]
            group = '%s %s' % (grouptype, name)
            
            oLine = [
                reference,
                source,
                _type,
                start,
                end,
                '.',
                strand[direction],
                '.',
                group
            ]

            writer.writerow(oLine)

            # New gene so blank these
            cdsStart = None
            cdsEnd = None
        elif line[0]=='+': # Translated region
            x = line.split(' ')
            cdsStart = int(x[1]) + offset
            cdsEnd = int(x[2]) + offset
        else:
            x = line.split(' ')
            start = int(x[0]) + offset
            end = int(x[1]) + offset

            if cdsStart==None or cdsEnd==None:
                oLine = [reference, source, 'CDS', start, end, '.', strand[direction], '.', group]
                writer.writerow(oLine)            
            if end<cdsStart or start>cdsEnd: # UTR
                oLine = [reference, source, 'UTR', start, end, '.', strand[direction], '.', group]
                writer.writerow(oLine)
            elif start>cdsStart and end<cdsEnd: # CDS
                oLine = [reference, source, 'CDS', start, end, '.', strand[direction], '.', group]
                writer.writerow(oLine)
            elif start<cdsStart and end>cdsStart: # UTR + CDS
                oLine = [reference, source, 'UTR', start, cdsStart-1, '.', strand[direction], '.', group]
                writer.writerow(oLine)
                oLine = [reference, source, 'CDS', cdsStart, end, '.', strand[direction], '.', group]
                writer.writerow(oLine)
            elif start<cdsEnd and end>cdsEnd: # CDS + UTR
                oLine = [reference, source, 'CDS', start, cdsEnd, '.', strand[direction], '.', group]
                writer.writerow(oLine)
                oLine = [reference, source, 'UTR', cdsEnd+1, end, '.', strand[direction], '.', group]
                writer.writerow(oLine)


if __name__=='__main__':
    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv)<5:
        sys.exit(__doc__)

    try:
        iFilename = sys.argv[1]
        oFilename = sys.argv[2]
        reference = sys.argv[3]
        source = sys.argv[4]
        offset = 0
        if len(sys.argv)==6:
            offset = int(sys.argv[5])
    except Exception:
        print "Error obtaining args"
        sys.exit(__doc__)
    

    exons2gff(iFilename, oFilename, reference, source, offset)

