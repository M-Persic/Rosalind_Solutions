def TranscribingDNAIntoRNA(dataset):
    """Convert a given DNA sequence into its RNA equivalent"""
    
    RNASeq = ""
    with open(dataset) as dataset:
        DNA = dataset.read().strip()
        for sequence in DNA:
            for nucleotide in sequence:
                RNASeq += "U" if nucleotide == "T" else nucleotide
    return RNASeq

if __name__ == '__main__':
    print(TranscribingDNAIntoRNA("rosalind_rna.txt"))
