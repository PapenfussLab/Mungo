#!/usr/bin/env python

"""
checkResults.py

Author: Tony Papenfuss
Date: Thu Sep 14 12:18:46 EST 2006

"""

import os, sys
import glob
import sets
import fasta, hmmer
from genomescan import parseGenscan
from useful import extractRootName


def testPeptide(seq):
    warnings = []
    errors = []
    
    if len(seq)==0:
        errors.append('No predicted protein')
        return
    elif len(seq)>1000:
        errors.append('Way too long')
    elif len(seq)>190:
        warnings.append('Kinda long (kept for now)')
    
    if seq[0]=='X': errors.append('No init')
    if seq[-1]=='X': errors.append('No term')
    
    return warnings,errors


def testAnnotation(prediction):
    warnings = []
    errors = []
    
    hasInit = False
    hasTerm = False
    nExons = 0
    for exon in prediction:
        if exon.type in ['Init','Intr','Term','Sngl']: nExons += 1
        if exon.type=='Init':
            hasInit = True
        elif exon.type=='Term':
            hasTerm = True
        elif exon.type=='Intr':
            hasIntr = True
    
    if not hasInit: errors.append('No init')
    if not hasTerm: errors.append('No term')
    
    if nExons>3:
        errors.append('%i exons (>3)' % nExons)
    elif nExons==3:
        warnings.append('3 exons')
    
    if hasInit and hasTerm:
        isCoding = True
    else:
        isCoding = False
    
    return isCoding, warnings, errors


# ----------------------------------------------------------------------

ioDir = sys.argv[1]
os.chdir(ioDir)
oFile = open('checkResults.txt', 'w')
sys.stdout = oFile

hmmerModel = {
    'round1': '../../HMMs/Defensin_beta.hmm',
    'round2': '../../HMMs/Defensin_beta_new.hmm'}[ioDir]


writer = fasta.MfaWriter('peptides.fa')
annotFile = open('annot.txt', 'w')

annotFilenames = glob.glob('gsAnnotations/*.txt')
for annotFilename in annotFilenames:
    name = extractRootName(annotFilename)
    print '>>>', name + '\n'
    
    annotFilename = 'gsAnnotations/%s.txt' % name
    annotation = open(annotFilename).readlines()
    predictions = parseGenscan(annotation)
    
    pepFilename = 'gsPeptides/%s.fa' % name
    peptides = fasta.load_mfa(pepFilename)
    peptides = [(h.split()[0],s) for h,s in peptides]
    peptides = dict(peptides)
    
    print 'Lengths'
    for h in peptides:
        print h, len(peptides[h])
    print
    
    i = 1
    for prediction in predictions.values():
        for exon in prediction:
            print exon
        print
        
        isCoding,warnings,errors = testAnnotation(prediction)
        
        if isCoding and len(errors)==0:
            seq = peptides['%s.%i' % (name, i)]
            warnings2,errors2 = testPeptide(seq)
            
            if len(errors2)==0:
                print 'Annotation warnings:', warnings
                print 'Peptide warnings:  ', warnings2
                
                print '\nCODING!!!'
                if len(warnings2)>0:
                    h = '%s  %s' % (name, '; '.join(warnings2))
                else:
                    h = name
                writer.write(h, seq+'\n')
                
                for exon in prediction:
                    exon.gene_exon = name
                    print >> annotFile, exon
                print >> annotFile
        else:
            print 'Annotation warnings:', warnings
            print 'Annotation errors:  ', errors
        print
    
    hmmerFilename = 'gsPepHmmer/%s.txt' % name
    os.system('hmmsearch %s %s > %s' % (hmmerModel, pepFilename, hmmerFilename))
    domains = hmmer.loadDomains(hmmerFilename)
    if domains:
        print 'Defensin motifs:'
        for d in domains:
            print d
    else:
        print 'No defensin motifs'
    print
    print '='*80 + '\n'

writer.close()
annotFile.close()
oFile.close()
