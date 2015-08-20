# CAP3 standalone parsers

def parserGenerator(iFile):
    header = ''
    contents = []
    state = State.begin
    for line in iFile:
        line = line.rstrip()
        if not line:
            # Blank
            pass
        elif state==State.begin:
            if line[0]!='*':
                # Junk at top
                pass
            elif line[0]=='*':
                # First contig
                state = State.section1or2
                header = ''.join(line.replace('*', '').strip().split())
        elif state==State.section1or2:
            if line[0]=='*':
                # New contig
                yield header, contents
                header = ''.join(line.replace('*', '').strip().split())
                contents = []
            elif line==Tokens.endSection1:
                pass
            else:
                # Contents line
                contents.append(line)
    yield header, contents


def fullParserGenerator(iFile):
    contigName = ''
    readNames = []
    contained = {}
    aln = []
    state = State.begin
    for line in iFile:
        line = line.rstrip()
        if not line:
            # Blank
            pass
        elif state==State.begin:
            if line[0]!='*':
                # Junk at top
                pass
            elif line[0]=='*':
                # Section 1 - First contig
                state = State.section1
                contigName = ''.join(line.replace('*', '').split())
        elif state==State.section1:
            if line[0]=='*':
                # Section 1 - New contig
                yield State.section1,(contigName,readNames,contained)
                contigName = ''.join(line.replace('*', '').split())
                readNames = []
                contained = {}
            elif line[0]==' ':
                # Section 1 - Read name, contained
                tokens = line.strip().split()
                readNames.append(tokens[0])
                contained[tokens[0]] = tokens[-1]
            elif line==endSection1Token:
                # End of section 1
                yield State.section1,(contigName,readNames,contained)
                state = State.beginSection2
            elif line[0]!=' ':
                # Section 1 - Read name
                readNames.append(line)
        elif state==State.beginSection2 and line[0]=='*':
            # Section 2 - First contig
            state = State.section2
            contigName = ''.join(line.replace('*', '').split())
        elif state==State.section2:
            if line[0]=='*':
                # Section 2 - New contig
                yield State.section2,(contigName,'\n'.join(aln))
                contigName = ''.join(line.replace('*', '').split())
                aln = []
            elif line[0]!='*':
                # Section 2 - Line in alignment
                aln.append(line)
        else:
            raise Exception('cap3._fullParserGenerator')
    yield State.section2,(contigName,'\n'.join(aln))
