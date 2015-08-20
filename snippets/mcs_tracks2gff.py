#!/usr/bin/env python

"""
bed2gff.py <mcs.tracks> <mcs_tracks.gff> <chromosome|scaffold|contig|reference id>

Converts the bed format output of WebMCS to gff.

Notes:
    Bed format:
    chrom  start  end  name  score

    GFF format:
    reference  source  type  start  end  score  strand  phase  group
"""

import sys
import csv
import re


def bed2gff(iFilename, oFilename, chrom):
    # Open input & output files
    iFile = open(iFilename)
    oFile = open(oFilename, 'w')

    # Extract track name & description
    header = iFile.readline().strip()

    search = re.search(' name=".*?"', header)
    start = search.start()
    end = search.end()
    name = header[start:end].split('"')[-2]

    search = re.search(' description=".*?"', header)
    start = search.start()
    end = search.end()
    description = header[start:end].split('"')[-2]

    # Define reader & writer
    bedFields = ['track', 'start', 'end', 'id', 'score']
    reader = csv.DictReader(iFile, bedFields, dialect='excel-tab')

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

    writer = csv.DictWriter(oFile, gffFields, dialect='excel-tab')

    # Translate
    feature = name
    for bed in reader:
        gff = {
            'reference': chrom,
            'source': 'MCS',
            'type': 'MCS-phylo-95',
            'start': bed['start'],
            'end': bed['end'],
            'score': bed['score'],
            'strand': '+',
            'phase': '.',
            'group': bed['id']
        }
        writer.writerow(gff)

    iFile.close()
    oFile.close()

if __name__=='__main__':
    args = sys.argv

    if '-h' in args or '--help' in args or len(args)!=4:
        sys.exit(__doc__)

    iFilename = args[1]
    oFilename = args[2]
    chrom = args[3]

    bed2gff(iFilename, oFilename, chrom)
