#!/usr/bin/env python

"""
mcs.phylo2gff.py <mcs.phylo> <mcs_phylo.gff> <chromosome|scaffold|contig|reference id> <offset>

Convert MCS phylo score file to wiggle format
with compression (position scores to blocks)
"""

import sys
import csv
import copy


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


def mcs_phylo2gff(iFilename, oFilename, chrom, offset):
    iFile = open(iFilename)
    oFile = open(oFilename, 'w')

    writer = csv.DictWriter(oFile, gffFields, dialect='excel-tab')

    start = None
    score_old = None
    for line in iFile:
        if line[0]=='#': # comment
            pass
        else:
            i,score = line.split('\t')

            if start==None:
                start = int(i)
                score_old = float(score)
            else:
                end = int(i)

                score = float(score)
                if score!=score_old:
                    gff = {
                        'reference': chrom,
                        'source': 'MCS',
                        'type': 'MCS-phylo-score',
                        'start': start+offset,
                        'end': end+offset,
                        'score': score,
                        'strand': '+',
                        'phase': '.',
                        'group': 'Parsimony MCS'
                    }
                    writer.writerow(gff)
                    start = copy.copy(end)
                    score_old = copy.copy(score)
    iFile.close()
    oFile.close()


if __name__=='__main__':
    args = sys.argv

    if '-h' in args or '--help' in args or len(args)!=5:
        sys.exit(__doc__)

    try:
        iFilename = args[1]
        oFilename = args[2]
        chrom = args[3]
        offset = int(args[4])
    except Exception:
        print "Error obtaining args"
        sys.exit(__doc__)
     
    mcs_phylo2gff(iFilename, oFilename, chrom, offset)
