#!/usr/bin/env python

"""
test.py

Author: Tony Papenfuss
Date: Tue Mar 18 14:27:10 EST 2008

"""

import os, sys


def rule():
    print '-'*80


from fasta import FastaFile

f = FastaFile('HSP100.fa')
rule()
print 'readOne'
print f.readOne()
print f.readOne()
rule()
print 'readAll'
print f.readAll()
rule()
print 'Mapping'
f.asMapping()
print f

rule()
rule()

f = FastaFile('HSP100.fa', indexed=True, interface='container')

print "Iteration"
i = 0
for h,s in f:
    print h,s
    i += 1
    if i==4: break

print '---'
for h,s in f:
    print h,s

rule()

f.reset()
print "Slicing"
print " Indexed"
print f[0]
print
print f[2]
print
print f.readOne()
rule()
print " Slicing"
print f[5:8]
print
print f[0:2]
rule()

print "As mapping"
f.asMapping()
print f['5']
print
rule()
