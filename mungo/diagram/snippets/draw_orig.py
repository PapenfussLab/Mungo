#!/usr/bin/env python

"""
draw.py

Author: Tony Papenfuss
Date: Sat Jul 22 11:45:06 EST 2006

"""

import os, sys, glob
import hmmer, blast, blat
from useful import DSU

from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.textlabels import Label
from Glyphs import *
from Common import Mapping

dpi = 72
margin = 36
# xsize,ysize = dpi*12*3,300


class Window:
    def __init__(self,chrom,start,end,xsize,ysize):
        self.chrom = str(chrom)
        self.start = int(start)
        self.end = int(end)
        self.xsize = int(xsize)
        self.ysize = int(ysize)
    
    def __repr__(self):
        return '%s:%i-%i' % (self.chrom,self.start,self.end)


class Feature:
    fields = ['name','chrom','start','end','strand','eValue']
    format = '\t'.join(['%%(%s)s' % f for f in fields])
    
    def __init__(self,name,chrom,start,end,strand,eValue):
        self.name = name
        self.chrom = chrom
        if strand=='-' and start>end:
            self.start = end
            self.end = start
        else:
            self.start = start
            self.end = end
        self.strand = strand
        self.eValue = eValue
    
    def __repr__(self):
        return self.format % self.__dict__


def loadHmmerData(filename, eValueCutoff=0.1, basename='hmm'):
    domains = hmmer.loadDomains(filename, seqType='BlockSixFrame')
    data = []
    for i,d in enumerate(domains):
        if d.eValue<=eValueCutoff:
            # print d
            name = '%s%0.2i' % (basename, i)
            d.toGenomic()
            f = Feature(name,d.accession,d.sStart,d.sEnd,d.strand,d.eValue)
            print f
            data.append(f)
    data = DSU(data, lambda x: (x.chrom, x.start))
    return data


def loadFilteredBlastData(eValueCutoff=0.1):
    # Load blast hits that do not overlap hmmer hits
    hits = blast.load('data/rmhmmer2.txt')
    data = []
    for i,h in enumerate(hits):
        if h.eValue<=eValueCutoff:
            h.convertBlockToGenomeCoords()
            name = h.queryId.split('|')[3]
            f = Feature(name,h.subjectId,h.sStart,h.sEnd,h.strand(),h.eValue)
            print f
            data.append(f)
    data = DSU(data, lambda x: (x.chrom, x.start))
    return data


def loadBlastData(eValueCutoff=0.1):
    # Load all blast hits
    filenames = glob.glob('../DEFB/blast/blast/*.txt')
    data = []
    for i,filename in enumerate(filenames):
        bh = blast.loadBestHit(filename, eValueCutoff=0.1)
        if bh:
            bh.convertBlockToGenomeCoords()
            name = bh.queryId.split('|')[3]
            f = Feature(name,bh.subjectId,bh.sStart,bh.sEnd,bh.strand(),bh.eValue)
            print f
            data.append(f)
    data = DSU(data, lambda x: (x.chrom, x.start))
    return data


def loadGenes():
    filenames = ['data/DEFA.psl', 'data/DEFB.psl']
    data = []
    for filename in filenames:
        for b in blat.load_iter(filename):
            for delimiter in ['.', '-']:
                b.tName = b.tName.replace(delimiter, ' ')
            chrom,bStart,bEnd = b.tName.split()
            bStart,bEnd = int(bStart),int(bEnd)
            f = Feature(b.qName,chrom,bStart+b.tStart-1,bStart+b.tEnd-1,b.strand,0)
            print f
            data.append(f)
    data = DSU(data, lambda x: (x.chrom, x.start))
    return data


def tick_generator(start, end, n=10, convert=None):
    dp = float(end-start)/n
    for i in xrange(n+1):
        t = start + i*dp
        if convert:
            t = convert(t)
        yield t


def addAxis(drawing, xmap, y, fontSize=8, tickLen=4, minorTickLen=2, 
 nTicks=20, strokeWidth=1, minorStrokeWidth=0.5):
    line = Line(xmap.x0, y, xmap.x1, y, strokeWidth=strokeWidth)
    drawing.add(line)

    ticks = tick_generator(xmap.start, xmap.end, n=nTicks, convert=int)
    for p in ticks:
        x = xmap(p)
        line = Line(x, y, x, y-tickLen, strokeWidth=strokeWidth)
        drawing.add(line)
        s = Label()
        s.setOrigin(x, y-tickLen)
        s.setText(str(p))
        s.fontName = 'Helvetica'
        s.fontSize = fontSize
        s.textAnchor = 'middle'
        s.boxAnchor = 'n'
        drawing.add(s)

    minorticks = tick_generator(xmap.start, xmap.end, n=50, convert=int)
    for p in minorticks:
        x = xmap(p)
        line = Line(x, y, x, y-minorTickLen, strokeWidth=minorStrokeWidth)
        drawing.add(line)


def addGene(drawing, xmap, y, gene, glyph=Arrow, fillColor=colors.red, 
 height=12, fontSize=8, labeldy=3, labelAngle=90, textAnchor='start', 
 boxAnchor='w'):
    if gene.strand=='+':
        x1,x2 = xmap(gene.start), xmap(gene.end)
    else:
        x2,x1 = xmap(gene.start), xmap(gene.end)
    g = glyph()
    g.x = x1
    g.y = y + height
    g.length = x2-x1
    g.fillColor = fillColor
    g.fontSize = fontSize
    g.label = gene.name
    g.labeldy = labeldy
    g.labelAngle = labelAngle
    g.textAnchor = textAnchor
    g.boxAnchor = boxAnchor
    drawing.add(g)


def main(genes, hmmMatches1, hmmMatches2, hsps, cluster, window):
    drawing = Drawing(window.xsize, window.ysize)
    
    y = 50
    xmap = Mapping(margin,window.xsize-margin,window.start,window.end)
    addAxis(drawing, xmap, y)
    
    for f in genes:
        if f.chrom==window.chrom and \
         (window.start<=f.start<=window.end or \
         window.start<=f.end<=window.end):
            addGene(drawing, xmap, y+20, f, fillColor=colors.blue)
    
#     for f in hmmMatches1:
#         if f.chrom==window.chrom and \
#          (window.start<=f.start<=window.end or \
#          window.start<=f.end<=window.end):
#             addGene(drawing, xmap, y+120, f, fillColor=colors.green)
#     
#     for f in hmmMatches2:
#         if f.chrom==window.chrom and \
#          (window.start<=f.start<=window.end or \
#          window.start<=f.end<=window.end):
#             addGene(drawing, xmap, y+200, f, fillColor=colors.green)
#     
#     for f in hsps:
#         if f.chrom==window.chrom and \
#          (window.start<=f.start<=window.end or \
#          window.start<=f.end<=window.end):
#             addGene(drawing, xmap, y+280, f, fillColor=colors.red)
    
    # oFilename = 'diagramsWithFeatures/%s.pdf' % cluster
    oFilename = '%s.pdf' % cluster
    renderPDF.drawToFile(drawing, oFilename, '')
    os.system('open %s' % oFilename)


if __name__=='__main__':
    hmmMatches1 = loadHmmerData('data/DEFB_hmmer_round1.txt', basename='hmm_')
    hmmMatches2 = loadHmmerData('data/DEFB_hmmer_round2.txt', basename='hmm2_')
    hsps = loadBlastData()
    genes = loadGenes()
    
    # ysize = 450
    ysize = 150
    clusters = {
        'Cluster1': Window('1', 422125000, 422750000, dpi*12*2, ysize),
        'Cluster2': Window('1', 557250000, 559750000, dpi*12*3, ysize),
        'Cluster3': Window('2', 297075000, 297450000, dpi*12*2, ysize)
    }
    for cluster,window in clusters.iteritems():
        main(genes, hmmMatches1, hmmMatches2, hsps, cluster, window)
    

