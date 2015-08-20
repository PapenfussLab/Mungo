#!/usr/bin/env python

"""
test.py

Author: Tony Papenfuss
Date: Tue 17 Aug 2010 15:04:15 EST

"""

import os, sys
from mungo.hmmer3 import *
from mungo.fasta import *


dnaFilename = "seq/dna.fa"
pepFilename = "seq/6frames.fa"
hmmerFilename = "MHC_I_domtbl.txt"

pep1 = "SGPGSHTIQIMYGCDVGSDGRFLRGYRQDAYDGKDYIALNEDLRSWTAADMAAQITKRKWEAAHEAEQLRAYLDGTCVEWLRRYLENGKETL"
pep2 = "GSHSMRYFFTSVSRPGRGEPRFIAVGYVDDTQFVRFDSDAASQRMEPRAPWIEQEGPEYWDQETRNVKAQSQTDRVDLGTLRGYYNQSEAG"
dna1 = ""
dna2 = ""


dna = {}
for h,s in FastaFile(dnaFilename):
    acc = h.split()[0]
    dna[acc] = s

pep = {}
for h,s in FastaFile(pepFilename):
    acc = h.split()[0]
    pep[acc] = s


f = DomainHitsReader(hmmerFilename)
for domain in f:
    print domain
    print pep[domain.targetName][domain.alnStart-1:domain.alnEnd]
