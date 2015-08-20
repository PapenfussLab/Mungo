#!/usr/bin/env python

"""
mcs_phylo2wig.py <mcs.phylo> <mcs_phylo.wig> <chromosome|scaffold|contig|reference id> <offset> 

Convert MCS phylo score file to wiggle format 
with compression (position scores to blocks)

Note - Add lines

browser dense WebMCS_95
browser full MCS_Score

to top of mcs.track file to control UCSC genome browser.
"""

import sys
import copy


def mcs_phylo2wig(iFilename, oFilename, chrom, offset):
    iFile = open(iFilename)
    oFile = open(oFilename, 'w')

    print >> oFile, 'track type=wiggle_0 name="MCS_Score" description="MCS parsimony-based score" visibility=full'

    start = None
    score0 = None
    for line in iFile:
        if line[0]=='#': # comment
            pass
        else:
            i,score = line.split('\t')

            if start==None:
                start = int(i) + offset
                score0 = float(score)
            else:
                stop = int(i) + offset

                score = float(score)
                if score!=score0:
                    print >> oFile, "%s\t%i\t%i\t%5.3f" % (chrom, start, stop, score)
                    start = copy.copy(stop)
                    score0 = copy.copy(score)
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
    
    mcs_phylo2wig(iFilename, oFilename, chrom, offset)
    
