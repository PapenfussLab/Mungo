#!/usr/bin/env python

"""
runGenomescan.py

Author: Tony Papenfuss
Date: Thu Sep  7 22:27:54 EST 2006

"""


import os, sys
import glob
import StringIO

import fasta
from genomescan import *
from mungoCore import AbstractFeature


homeDir = os.environ['HOME']
blastDb = os.path.join(homeDir, 'databases/opossum/assembly/blastdb/assembly')


fields = ['domain', 'accession', 'count', 'sStart', 'sEnd', 'sCode',
    'qStart', 'qEnd', 'qCode', 'score', 'eValue', 'strand',
    'lowScoring', 'pseudogene', 'nCysteines']


class Feature(AbstractFeature):
    """Simple Feature class for use with genomescanFromFeature"""
    
    format = '\t'.join(['%%(%s)s' % field for field in fields])
    
    def __init__(self, *args, **kw):
        AbstractFeature.__init__(self, fields, *args, **kw)
    
    def convert(self):
        self.sStart = int(self.sStart)
        self.sEnd = int(self.sEnd)
        self.score = float(self.score)
        self.eValue = float(self.eValue)
    
    def __repr__(self):
        return Feature.format % self.__dict__


def loadFeaturesIter(iFilename):
    """Load curated defensin hmmer hits"""
    iFile = open(iFilename)
    line = iFile.next()
    for line in iFile:
        tokens = line.strip().split('\t')
        yield Feature(tokens)


def runGenomescan(features, debug=False):
    """Run genomescan supplying extracted features from genome as 
    homologous proteins."""
    
    for i,feature in enumerate(features):
        print i+1, feature
        oFilename = 'gsOutput/%s.html' % feature.domain
        annotFilename = 'gsAnnotations/%s.txt' % feature.domain
        pepFilename = 'gsPeptides/%s.fa' % feature.domain
        
        if not os.path.exists(oFilename):
            html = genomescanFromFeature(feature, blastDb, oFileHandle=oFilename)
        else:
            html = open(oFilename).read()
        
        html = html.split('\n')
        annotation, peptides = parseGenomeScanOutput(html)
        
        print >> open(annotFilename, 'w'), annotation
        
        fakeFaFile = StringIO.StringIO(peptides)
        faIter = fasta.load_iter(fakeFaFile)
        writer = fasta.MfaWriter(pepFilename)
        for j,(h,s) in enumerate(faIter):
            block = h.split('|')[0]
            if j==1: print feature
            h = '%s.%i %s' % (feature.domain, j+1, block)
            writer.write(h, s+'\n')
        writer.close()


if __name__=='__main__':
    ioDir = sys.argv[1]
    os.chdir(ioDir)
    if '-c' in sys.argv: os.system('rm gsOutput/*.html')
    features = loadFeaturesIter('DEFB_genomic.txt')
    runGenomescan(features)
