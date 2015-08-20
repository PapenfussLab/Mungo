#!/usr/bin/env python

"""
test.py

Author: Tony Papenfuss
Date: Wed Apr 16 23:26:05 EST 2008

"""


class TestFileIterator1:
    def __init__(self, iFilename):
        self.iFile = open(iFilename)
        
    def __iter__(self):
        self._iter = self._generator()
        return self
    
    def next(self):
        for d in self._iter:
            return d
        raise StopIteration
    
    def _generator(self):
        header = ''
        seq = []
        for line in self.iFile:
            line = line.strip()
            if line:
                if line[0]=='>':
                    if seq:
                        yield header, ''.join(seq)
                    header = line[1:]
                    seq = []
                else:
                    seq.append(line)
        if header and seq:
            yield header, ''.join(seq)


class TestFileIterator2:
    def __init__(self, iFilename):
        self.iFile = open(iFilename)
        
    def __iter__(self):
        return self
    
    def next(self):
        header = ''
        seq = []
        for line in self.iFile:
            line = line.strip()
            if line:
                if line[0]=='>':
                    if seq:
                        yield header, ''.join(seq)
                    header = line[1:]
                    seq = []
                else:
                    seq.append(line)
        if header and seq:
            yield header, ''.join(seq)


print 'TestFileIterator1, file1'
f = TestFileIterator1('test1.txt')
for h,s in f11:
    print h,s
print

print 'TestFileIterator1, file2'
f = TestFileIterator1('test2.txt')
for h,s in f2:
    print (h,s)
print

print 'TestFileIterator2, file1'
f = TestFileIterator2('test1.txt')
for h,s in f:
    print h,s
print
