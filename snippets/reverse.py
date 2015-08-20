#!/usr/bin/env python

"""
reverse.py <input>

Prints the contents of <input> in reverse order
"""

import sys

if len(sys.argv)==1 or '-h' in sys.argv or '--help' in sys.argv:
    sys.exit(__doc__)


iFile = open(sys.argv[1])

data = []
for line in iFile:
    data.append(line.strip())

data.reverse()

for line in data:
    print line
