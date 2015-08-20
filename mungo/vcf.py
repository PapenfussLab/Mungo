"""
vcf.py
"""

class VCFEntry:
    def __init__(self, tokens):
        self.chrom = tokens[0]
        self.pos = int(tokens[1])
        self.id = tokens[2]
        self.ref = tokens[3]
        self.alt = tokens[4]
        self.qual = tokens[5]
        self.filter = tokens[6]
        self.info = tokens[7]
        if len(tokens)>=10:
            self.format = tokens[8]
            self.samples = tokens[9:]
            self.coverage = int(self.get_info("ADP"))
    
    def get_info(self, key=None):
        d = dict([tuple(x.split("=")) for x in self.info.split(";")])
        if key:
             return d[key]
        else:
            return d
    
    def get_sample_data(self, key=None, sample=1):
        a = self.format.split(":")
        b = self.samples[sample-1].split(":")
        d = dict(zip(a,b))
        if key:
             return d[key]
        else:
            return d
    
    def __repr__(self):
        return "\t".join(["%(chrom)s", "%(pos)i", "%(id)s", "%(ref)s", "%(alt)s", "%(qual)s", "%(filter)s", "%(info)s", "%(format)s", "%(sample1)s"]) % self.__dict__
    
    @staticmethod
    def load(input_filename, include_reject=False):
        headers = []
        data = []
        for line in open(input_filename):
            if line[0]=="#": 
                headers.append(line)
                continue
            tokens = line.strip().split("\t")
            d = VCFEntry(tokens)
            if not include_reject and d.filter=="REJECT":
                continue
            else:
                data.append(d)
        return headers,data


