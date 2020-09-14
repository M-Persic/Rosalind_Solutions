def ComputingGCContent(dataset):
    """Return the GC content of given DNA sequences following a FASTA format"""

    sequences = {}
    with open(dataset) as dataset:
        fastaLine = dataset.readlines()
        for line in range(0, len(fastaLine)):
            if '>' in fastaLine[line]:
                seqID, seqLength, GCCounter = fastaLine[line], 0, 0 
                line += 1
                while (line != len(fastaLine) and '>' not in fastaLine[line]):
                    seqLength += len(fastaLine[line].strip())
                    GCCounter += (fastaLine[line].count('G') + fastaLine[line].count('C'))
                    line += 1
                sequences.update({seqID: (GCCounter/seqLength) * 100})
        highestSeq = max(sequences, key=sequences.get)
    return "{0}{1:.06f}".format(highestSeq.replace('>', ''), round(sequences.get(highestSeq), 6)) 


if __name__ == '__main__':
    print(ComputingGCContent("rosalind_gc.txt"))
