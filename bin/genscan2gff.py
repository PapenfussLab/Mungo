#!/usr/bin/env python

"""
genscan2gff.py [options] <genscan/genomescan file> <reference> <source> <class>
"""

import sys
from optparse import OptionParser

import mungo.gff
import mungo.genscan as genscan
from mungo.useful import DSU, smartopen


if __name__=="__main__":
    usage = "%prog [options] <genscan file> <reference> <source> <class>"
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-o", "--output", 
        dest="output",
        help="Output filename (Default: stdout)", 
        default=None)
    parser.add_option(
        "-f", "--offset", 
        dest="offset",
        type="int",
        help="Coordinate offset",
        default=0)
    parser.add_option(
        "-u", "--unprocessed", 
        dest="unprocessed",
        action="store_true",
        help="Output is unprocessed (Default: False)",
        default=False)
    parser.add_option(
        "-t", "--types", 
        dest="types",
        help="Types (Default: mRNA,CDS)",
        default="mRNA,CDS")
    options, args = parser.parse_args(sys.argv)
    
    if len(args)!=5:
        sys.exit(__doc__)
    iFilename = args[1]
    reference = args[2]
    source = args[3]
    _class = args[4]
    
    if options.unprocessed:
        data = genscan.load(iFilename)
    else:
        data = genscan.load_preprocessed(iFilename)
    
    if not options.output or options.output=='stdout':
        writer = gff.GFFWriter(sys.stdout)
    else:
        writer = gff.GFFWriter(options.output)
    
    mainType,subType = options.types.split(',')
    
    for gene in data:
        out = []
        extrema = []
        for exon in gene:
            if exon.type in ['Init','Intr','Term','Sngl']:
                start,end=exon.start+options.offset,exon.end+options.offset
                if exon.strand=='-':
                    start,end = end,start
                extrema.append(start)
                extrema.append(end)
                g = gff.Feature(
                    reference=reference,
                    source=source,
                    type=subType,
                    start=start,
                    end=end,
                    strand=exon.strand,
                    group='%s %s' % (_class, exon.gene_exon.split('.')[0])
                )
                out.append(g)
        if out:
            out = DSU(out, lambda x: x.start)
            g = gff.Feature(
                reference=out[0].reference,
                source=out[0].source,
                type=mainType,
                start=min(extrema),
                end=max(extrema),
                strand=out[0].strand,
                group=out[0].group
            )
            out.insert(0,g)
            for g in out:
                writer.write(g)
    writer.close()
