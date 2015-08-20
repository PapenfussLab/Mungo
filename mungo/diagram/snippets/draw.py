#!/usr/bin/env python

"""
draw.py

Author: Tony Papenfuss
Date: Sun Oct 22 15:48:47 EST 2006

"""

import os, sys, copy
import generic
from diagram import *
from useful import DSU


xsize = A4Portrait.width
ysize = A4Portrait.height
margin = 0.5*DPI

data = generic.load('LRC_wider_search2.txt', 
    converters={'sStart': int, 'sEnd': int})
data = DSU(data, lambda x: x.sStart)

geneColor = {'NA': colors.green, '1': colors.orange, '2': colors.blue}

chains = [(7,8),(9,10,11,12,13),(16,17,18),(20,21,22),
    (24,25,26),(27,28),(29,30,31),(37,38),(45,46),
    (52,53),(54,55),(56,57),(59,60,61),(63,64,65),
    (69,70),(72,73),(76,77),(81,82),(83,84),(93,94,95)]

clusters = [
    ('Cluster1', 370810000, 371794000),
    ('Cluster2', 372679000, 373860000),
    ('Cluster3', 378430000, 379620000),
    ('Cluster4', 395530000, 397060000),
    ('Cluster5', 399550000, 400500000),
    ('Cluster6', 404080000, 404680000),
]
L = max([cluster[2]-cluster[1] for cluster in clusters])
L = 1000*(L/1000)

drawing = Drawing(xsize, ysize)
xmap = Mapping(margin, xsize-margin, 0, L)
scale = xmap.scale

trackHeight = (ysize-0.5*margin)/len(clusters)
print trackHeight

y = margin
for cluster,start,end in clusters:
    print 'Length:', end-start
    xmap = Mapping.fromScale(margin, start, end, scale)
    
    s = Label()
    s.setText('--- 1 ---')
    s.setOrigin(0.5*margin, y)
    drawing.add(s)
    
    # Axis
    y += 40
    s = Label()
    s.setText('--- 2 ---')
    s.setOrigin(0.5*margin, y)
    drawing.add(s)
    
    nTicks = int(round((end-start)/1e5))
    nMinorTicks = int(round((end-start)/1e4))
    addAxis(drawing, xmap, y, nTicks=nTicks, nMinorTicks=nMinorTicks,
        fontSize=16, scale=1e5)

    # Features
    y += 20
    s = Label()
    s.setText('--- 3 ---')
    s.setOrigin(0.5*margin, y)
    drawing.add(s)
    
    for f in data:
        if f.sStart>=start and f.sEnd<=end:
            f.name = f.domain
            f.start = f.sStart
            f.end = f.sEnd
            addFeature(drawing, xmap, y, f, fillColor=geneColor[f.type],
                height=40, fontSize=16, wmin=7, wNoTail=10)
    
    y += 150
    s = Label()
    s.setText('--- 4 ---')
    s.setOrigin(0.5*margin, y)
    drawing.add(s)
    
    for chain in chains:
        chainsFullNames = ['LRC%0.3i' % i for i in chain]
        features = [f for f in data if f.domain in chainsFullNames]
        chainStart = features[0].sStart
        chainEnd = features[-1].sEnd
        if chainStart>=start and chainEnd<=end:
            zoomMap = Mapping.fromScale(
                xmap(chainStart),chainStart,chainEnd,50*scale)
            g = Group()
            g.translate(-0.5*(zoomMap.x1-zoomMap.x0), y)
            
            for f in features:
                addFeature(g, zoomMap, 0, f, fillColor=geneColor[f.type],
                    fontSize=20, labelAngle=90, labeldy=5)
            
            fLast = features[0]
            for f in features[1:]:
                addRuler(g, zoomMap, 10, fLast.end, f.start, 
                    tickLen=5, strokeWidth=0.25, scale=1, format='%ibp')
                fLast = copy.copy(f)
            drawing.add(g)
    y += (trackHeight-40-20-150)
oFilename = 'LRC.pdf'
renderPDF.drawToFile(drawing, oFilename, '')
os.system('open %s' % oFilename)
