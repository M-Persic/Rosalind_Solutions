import numpy as np

def ConsensusAndProfile(dataset):
    """Determine the consensus sequence of given DNA strings in a FASTA format"""
    
    with open(dataset) as dataset:
        fasta = dataset.read().split("\n")
        DNAStrings = [fasta[i] for i in range(len(fasta)) if not fasta[i].startswith(">")]
        profileMatrix = np.empty((4,len(DNAStrings[0])), int)
        
if __name__ == '__main__':
    print(ConsensusAndProfile("rosalind_cons.txt"))
