from alchemy import *
from blast import BlastFile, HSP


h = HSP()
metadata = MetaData()
hsps_table = createTable("HSPs", metadata, h.attributes, h.converters)
mapper(HSP, hsps_table)

engine = create_engine("sqlite:///test2.db")
metadata.create_all(engine)

Session = sessionmaker(autoflush=True, transactional=True)
Session.configure(bind=engine)
session = Session()

filename = '/Users/papenfuss/databases/devil/transcriptome/reads/blast_results/blastn_tumour_v_opossum.txt'
for h in BlastFile(filename):
    session.save(h)
    break
session.commit()
