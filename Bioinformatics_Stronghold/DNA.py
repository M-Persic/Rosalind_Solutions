def CountingDNANucleotides(dataset):
    """Return the frequency of each nucleotide in a given DNA sequence"""
    
    nucleotideFrequency = {"A":0,"C":0,"G":0,"T":0}
    with open(dataset) as DNA:
        DNA = DNA.read().strip()
        for sequence in DNA:
            for nucleotide in sequence:
                nucleotideFrequency[nucleotide] = nucleotideFrequency.get(nucleotide) + 1
    return "{A} {C} {G} {T}".format(**nucleotideFrequency)

if __name__ == '__main__':
    print(CountngDNANucleotides("rosalind_dna.txt"))
                
