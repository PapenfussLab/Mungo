#!/usr/bin/env python

import re
import Fasta


classes = {
    'Extended B': (14850000, 15460000),
    'Class I-II': (15460000, 17100000),
    'Class III': (17100000, 17950000),
    'Framework': (17950000, 19265000),
    'Extended A': (19265000, 19400000)
}

header,seq = Fasta.load('scaffold_42.fa')

for name,(start,end) in classes.items():
    name = '_'.join(name.split())
    new_header = '%s.%s-%s' % (header, start, end)
    Fasta.save('%s.fa' % name, new_header, seq[start-1:end])
    
