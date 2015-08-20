#!/usr/bin/env python

"""
extractHmmerResults.py <ioDir>

Input: Hmmer output 'DEFB.txt'

Outputs:
    - the genomic version (DEFB_genomic.txt)
    - a summary (DEFB_summary.txt)
    - extracted sequence (DEFB_extracted.fa)
    - the translation of this (DEFB_extracted_pep.fa)

Author: Tony Papenfuss
Date: Tue Aug 15 10:18:46 EST 2006

"""

import os, sys
import hmmer, fasta, sequence


homeDir = os.environ['HOME']
blastdb = os.path.join(homeDir, 'databases/opossum/assembly/blastdb/assembly')


ioDir = sys.argv[1]
os.chdir(ioDir)

genomicFile = open('DEFB_genomic.txt', 'w')
summaryFile = open('DEFB_summary.txt', 'w')
dnaWriter = fasta.MfaWriter('DEFB_extracted.fa')
pepWriter = fasta.MfaWriter('DEFB_extracted_pep.fa')

domains = hmmer.loadDomains('DEFB.txt', seqType='BlockSixFrame')
print >> genomicFile, '\t'.join(domains[0].fields 
    + ['strand', 'lowScoring', 'pseudogene', 'nCysteines'])

for i,domain in enumerate(domains):
    if i>99: break
    domain.domain = 'DEFB_%0.2i' % (i+1)
    domain.toGenomic(relative=True)
    domain.addField('lowScoring', 'N')
    domain.addField('pseudogene', 'N')
    domain.addField('nCysteines', 0)
    summary = []
    
    h,s = fasta.getSequence(blastdb, domain.accession, 
        start=domain.sStart, end=domain.sEnd, strand=domain.strand)
    pep = sequence.translate(s)
    
    if i>59: domain.lowScoring = 'Y'
    if '*' in pep:
        domain.pseudogene = 'Y'
        summary.append('Contains stops')
    
    for aa in pep:
        if aa=='C':
            domain.nCysteines += 1
    if domain.nCysteines!=6:
        summary.append('Has %i cysteines' % domain.nCysteines)
    
    print >> summaryFile, '%s\t%s' % (domain.domain, '; '.join(summary))
    
    if domain.pseudogene=='Y' or domain.nCysteines<5 or domain.nCysteines>7:
        print 'Skipped', i
    else:
        h2 = '%s  %s:%s-%s(%s)' % (domain.domain, domain.accession, domain.sStart, domain.sEnd, domain.strand)
        dnaWriter.write(h2, s + '\n')
        pepWriter.write(h2, pep + '\n')
        print >> genomicFile, domain

genomicFile.close()
summaryFile.close()
dnaWriter.close()
pepWriter.close()
