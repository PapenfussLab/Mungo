#!/usr/bin/env python

import Genscan
import GFF


meta, data, proteins = Genscan.load('genscan.txt')

offset = 16000000

reference = 'scaffold_42'
gffSource = 'genscan'
gffClass = 'Genscan'
featureType = 'gene'
subfeatureType = 'exon'

for gene in data:
    name = gene[0]['gene.exon'].split('.')[0]
    output = []
    extrema = []
    for exon in gene:
        if exon['type'] in ['Init','Intr','Term','Sngl']:
            output.append(GFF.output(
                reference = reference,
                source = gffSource,
                type = subfeatureType,
                start = exon['start']+offset-1,
                end = exon['end']+offset-1,
                strand = exon['strand'],
                score = exon['score'],
                group = '%s %s' % (gffClass, name)
            ))
            extrema.append(exon['start'])
            extrema.append(exon['end'])

    output.insert(0, GFF.output(
        reference = 'scaffold_42',
        source = gffSource,
        type = featureType,
        start = min(extrema)+offset-1,
        end = max(extrema)+offset-1,
        strand = gene[0]['strand'],
        group = '%s %s' % (gffClass, name)
    ))

    for out in output:
        print out
