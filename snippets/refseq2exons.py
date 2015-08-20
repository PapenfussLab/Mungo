#!/usr/bin/env python

"""
refseq2exons.py <refseq file> <exons file> <offset>
"""

import sys
import os
import csv


def refseq2exons(iFilename, oFilename, offset):
    # Build translation table
    iDir = '/Users/papenfuss/data/databases/human'
    filename = os.path.join(iDir, 'refLink.txt')
    dataFile = open(filename)
    reader = csv.reader(dataFile, dialect='excel-tab')
    translate = {}
    for line in reader:
        translate[line[2]] = line[0]
    dataFile.close()
    
    # Parse the annotation file & convert to PIP format
    iFile = open(iFilename)
    headers = iFile.readline().strip()[1:].split('\t')
    reader = csv.DictReader(iFile, headers, dialect='excel-tab')

    oFile = open(oFilename, 'w')

    def convertAndShift(base, offset):
        return int(base) - offset
    shift = convertAndShift

    # > forward strand
    # < reverse strand
    symbol = {"+":">", "-":"<"}

    for d in reader:
        start = shift(d['txStart'], offset)
        end = shift(d['txEnd'], offset)

        cdsStart = shift(d['cdsStart'], offset)
        cdsEnd = shift(d['cdsEnd'], offset)

        name = d['name']
        try:
            name = translate[name]
        except Exception:
            pass
        
        print >> oFile, symbol[d['strand']], start, end, name            
        print >> oFile, '+', cdsStart, cdsEnd

        exonStarts = d['exonStarts'][0:-1].split(',')
        exonEnds = d['exonEnds'][0:-1].split(',')
        for start,end in zip(exonStarts, exonEnds):
            print >> oFile, shift(start, offset),shift(end, offset)

if __name__=='__main__':
    args = sys.argv

    if '-h' in args or '--help' in args or len(args)!=4:
        sys.exit(__doc__)

    try:
        iFilename = args[1]
        oFilename = args[2]
        offset = int(args[3])
    except Exception:
        print "Error obtaining args"
        sys.exit(__doc__)
     
    refseq2exons(iFilename, oFilename, offset)

