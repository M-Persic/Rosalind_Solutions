def ComplementingAStrandOfDNA(dataset):
    """Convert a given DNA seq into its complementary counterpart (5'-3)"""

    complementarySeq = ""
    complementaryNucleotide = {"A":"T", "T": "A", "G":"C", "C":"G"}
    with open(dataset) as dataset:
        seq = dataset.read().strip()
    return "".join(complementaryNucleotide.get(nucleotide) for nucleotide in seq[::-1])

if __name__ == '__main__':
    print(ComplementingAStrandOfDNA("rosalind_revc.txt"))
