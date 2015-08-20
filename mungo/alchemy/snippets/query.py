#!/usr/bin/env python

"""
snippet.py

Author: Tony Papenfuss
Date: Mon Jun 23 23:32:21 EST 2008

"""

import os, sys
from alchemy import *
from blast import BlastFile, HSP


tableName = 'Devil454'  # Devil454, Platy454, PlatySolexa
dsn = 'sqlite:///test.db'


metadata = MetaData()

# Create the table and define the mapping
h = HSP()
hsps_table = createTable(tableName, metadata, h.attributes, h.converters)
mapper(HSP, hsps_table)

# Start a session & initialize database
session = startSession(dsn, metadata)


for h in session.query(HSP).filter(HSP.subjectId=='3'):
    print dir(h)
    print h
