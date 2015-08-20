#!/usr/bin/env python

"""
bed2gff.py <BED file>
"""

import sys
import gff
import bed


if '-h' in sys.argv or len(sys.argv)!=2:
    sys.exit(__doc__)

data = bed.load(sys.argv[1])

for element in data:
    g = gff.Feature(
        reference='CR925799',
        source='most-cons',
        type='motif',
        start=element.chromStart,
        end=element.chromEnd,
        group='Motif %s' % element.name)
    print g
