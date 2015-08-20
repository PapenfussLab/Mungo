#!/usr/bin/env python

"""
test.py

Author: Tony Papenfuss
Date: Mon Jun 23 22:35:08 EST 2008

"""

import os, sys
from sqlalchemy import MetaData, Table, Column, Integer, Float, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, sessionmaker, relation
from sqlalchemy.sql.expression import join
from blast import BlastFile, HSP


metadata = MetaData()
hsp_table = Table("HSPs", metadata,
    Column('id', Integer, primary_key=True),
    Column('queryId', Text),
    Column('subjectId', Text),
    Column('pcId', Float),
    Column('alignLength', Float),
    Column('matches', Integer),
    Column('mismatches', Integer),
    Column('qStart', Integer),
    Column('qEnd', Integer),
    Column('sStart', Integer),
    Column('sEnd', Integer),
    Column('eValue', Float),
    Column('bitScore', Float)
)

mapper(HSP, hsp_table)

engine = create_engine("sqlite:///test.sqlite3")
metadata.create_all(engine)

Session = sessionmaker(autoflush=True, transactional=True)
Session.configure(bind=engine)
session = Session()

filename = '/Users/papenfuss/databases/devil/transcriptome/reads/blast_results/blastn_tumour_v_opossum.txt'
for i,h in enumerate(BlastFile(filename)):
    h.convertBlockToGenomeCoords()
    session.save(h)
    if i==10: break
session.commit()
