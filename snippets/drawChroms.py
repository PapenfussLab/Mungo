#!/usr/bin/env python

"""
draw.py

Author: Tony Papenfuss
Date: Thu Aug 28 14:21:49 EST 2008

"""

import os, sys
from math import log, log10
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.axes import XValueAxis 


DPI = 300
XSIZE,YSIZE = 24/2.54*DPI,18/2.54*DPI
MARGIN = DPI


chrSizes = {
    '1': 748055161,
    '2': 541556283,
    '3': 527952102,
    '4': 435153693,
    '5': 304825324,
    '6': 292091736,
    '7': 260857928,
    '8': 312544902,
    'X': 79335909,
    'Un': 103241611,
    'MT': 17079
}


class Feature:
    def __init(self):
        pass


class Mapping:
    """Map from base coordinates to pixels"""
    def __init__(self, x0, x1, start, end):
        self.x0 = x0
        self.x1 = x1
        self.start = start
        self.end = end

    def __call__(self, i):
        dx = float(self.x1-self.x0)
        dp = float(self.end-self.start)
        return self.x0 + dx/dp*(i-self.start)


def addChromosomes(drawing, chrNames, chrSizes, xmap, ymap, w=0.1*DPI, fillColor=colors.skyblue, strokeColor=colors.skyblue):
    for i,chrom in enumerate(chrNames):
        x = xmap(i+1)
        y = ymap(chrSizes[chrom])
        h = ymap(1)-ymap(chrSizes[chrom])
        
        chromosome = Rect(x,y,w,h, strokeColor=strokeColor, fillColor=fillColor)
        drawing.add(chromosome)
        
        topCap = Wedge(x+0.5*w, y+h, 0.5*w, 0, 180, strokeColor=strokeColor, fillColor=fillColor)
        bottomCap = Wedge(x+0.5*w, y, 0.5*w, 180, 0, strokeColor=strokeColor, fillColor=fillColor)
        drawing.add(topCap)
        drawing.add(bottomCap)
        
        label = Label()
        label.setOrigin(xmap(i+1)+w/2, ymap(0))
        label.boxAnchor = 's'
        label.textAnchor = 'middle'
        label.dx = 0
        label.dy = DPI/10
        label.setText(chrom)
        label.fontSize = 36
        label.fontName = 'Helvetica'
        drawing.add(label)
        
        chrLength = Label()
        chrLength.setOrigin(xmap(i+1)+w/2, ymap(chrSizes[chrom]))
        chrLength.boxAnchor = 'n'
        chrLength.textAnchor = 'middle'
        chrLength.dx = 0
        chrLength.dy = -DPI/10
        chrLength.setText('%iMb' % int(chrSizes[chrom]/1e6))
        chrLength.fontSize = 24
        chrLength.fontName = 'Helvetica'
        drawing.add(chrLength)


# def addFeatureCountsAsPoints(drawing, geneCounts, chrPos, xmap, ymap, w_chrom=0.1*DPI, dx=6, strokeWidth=0):
#     cmax = 0
#     scale = 12
#     mylog = log10
#     for geneCount in geneCounts:
#         i = chrPos[geneCount.chrom]
#         
#         # Tumour
#         x1 = xmap(i) + w_chrom + dx
#         y = ymap(geneCount.start)
#         if geneCount.tumour==0:
#             x2 = x1
#         else:
#             x2 = x1 + scale*(1+mylog(geneCount.tumour))
#             cmax = max(cmax, geneCount.tumour)
#         r = Rect(x2, y, 1, 1, strokeColor=colors.black, strokeWidth=strokeWidth)
#         drawing.add(r)
#         
#         # Testis
#         x1 = xmap(i)-1-dx
#         if geneCount.testis==0:
#             x2 = x1
#         else:
#             x2 = x1 - scale*(1+mylog(geneCount.testis))
#             cmax = max(cmax, geneCount.testis)
#         q = Rect(x2, y, 1, 1, strokeColor=colors.red, strokeWidth=strokeWidth)
#         drawing.add(q)
#     
#     cmin = 1
#     data = [(mylog(cmin), mylog(cmax)), (0, 0)]
#     xAxis = XValueAxis()
#     i = chrPos['1']
#     x = xmap(i) + w_chrom + dx + scale
#     xAxis.setPosition(x, ymap(0)+25, scale*(1+mylog(cmax)))
#     xAxis.configure(data)
#     drawing.add(xAxis)
# 
# 
# def addFeatureCounts(drawing, features, chrPos, xmap, ymap, scale=10, 
#  w_chrom=0.1*DPI, dx=6, strokeWidth=1, style='line'):
#     mylog = log10
#     for feature in features:
#         i = chrPos[feature.chrom]
#         
#         # Tumour
#         x1 = xmap(i) + w_chrom + dx
#         y1 = ymap(feature.start)
#         y2 = ymap(feature.end)
#         y = 0.5*(y1+y2)
#         if feature.tumour==0:
#             x2 = x1
#         else:
#             x2 = x1 + scale*(1+mylog(feature.tumour))
#         
#         if style=='block':
#             r = Rect(x1, y1, x2-x1, y2-y1, fillColor=colors.black, 
#                 strokeColor=colors.black, strokeWidth=strokeWidth)
#         elif style=='line':
#             r = Line(x1, y, x2, y, fillColor=colors.black, 
#                 strokeColor=colors.black, strokeWidth=strokeWidth)
#         elif style=='point':
#             r = Rect(x2, y, 2, 2, strokeColor=colors.black, strokeWidth=strokeWidth)
#         drawing.add(r)
#         
#         # Testis
#         x1 = xmap(i)-1-dx
#         if feature.testis==0:
#             x2 = x1
#         else:
#             x2 = x1 - scale*(1+mylog(feature.testis))
#         
#         if style=='block':
#             r = Rect(x1, y1, x2-x1, y2-y1, fillColor=colors.red, 
#                 strokeColor=colors.red, strokeWidth=strokeWidth)
#         elif style=='line':
#             r = Line(x1, y, x2, y, fillColor=colors.red, 
#                 strokeColor=colors.red, strokeWidth=strokeWidth)
#         elif style=='point':
#             r = Rect(x2, y, 2, 2, strokeColor=colors.red, strokeWidth=strokeWidth)
#         drawing.add(r)


def draw(drawing, chrNames, chrPos, chrSizes):
    # Mappings
    xmap = Mapping(MARGIN, XSIZE-MARGIN, 1, 10)
    
    # Based on largest chromosome only with 0 at top
    ymap = Mapping(YSIZE-MARGIN, MARGIN, 1, max(chrSizes.values()))
    
    addChromosomes(drawing, chrNames, chrSizes, xmap, ymap)


if __name__=='__main__':
    chrNames = ['%i' % i for i in xrange(1,9)] + ['X', 'Un']
    chrPos = dict(zip(chrNames, range(1,11)))
    
    drawing = Drawing(XSIZE, YSIZE)
    draw(drawing, chrNames, chrPos, chrSizes)
    
    renderPDF.drawToFile(drawing, 'diagram.pdf', '')
    os.system('open diagram.pdf')
