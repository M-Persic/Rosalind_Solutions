def FindingAMotifInDNA(dataset):
    """Find a motif in a given DNA sequence and return the motif's position(s)"""

    motifPositions = []
    with open(dataset) as dataset:
        sequences = dataset.read().splitlines()
        motifPositions = [sequences[0][i:].startswith(sequences[1]) for i in range(len(sequences[0]) - len(sequences[1]) + 1)] 
    return " ".join(str(position + 1) for position, foundMotif in enumerate(motifPositions) if foundMotif)

if __name__ == '__main__':
    print(FindingAMotifInDNA("rosalind_subs.txt"))
