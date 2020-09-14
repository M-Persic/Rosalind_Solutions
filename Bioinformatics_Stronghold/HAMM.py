def CountingPointMutations(dataset):
    """Return the Hamming distance between 2 given DNA sequences"""

    with open(dataset) as dataset:
        sequences = dataset.read().splitlines()
    return len([sequences[0][i] for i in range(0, len(sequences[0])) if sequences[0][i] != sequences[1][i]])

if __name__ == '__main__':
    print(CountingPointMutations("rosalind_hamm.txt"))
    
