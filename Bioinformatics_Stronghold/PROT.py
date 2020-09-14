def TranslatingRNAIntoProtein(dataset):
    """Translate a given RNA sequence into its protein string"""
    
    codonTable = {'F' : ['UUU', 'UUC'],
                  'L' : ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
                  'S' : ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                  'Y' : ['UAU', 'UAC'],
                  #STOP CODON
                  '' : ['UAA', 'UAG', 'UGA'],
                  'C' : ['UGU', 'UGC'],
                  'W' : ['UGG'],
                  'P' : ['CCU', 'CCC', 'CCA', 'CCG'],
                  'H' : ['CAU', 'CAC'], 
                  'Q' : ['CAA', 'CAG'],
                  'R' : ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                  'I' : ['AUU', 'AUC', 'AUA', 'AUA'],
                  'M' : ['AUG'],
                  'T' : ['ACU', 'ACC', 'ACA', 'ACG'],
                  'N' : ['AAU', 'AAC'],
                  'K' : ['AAA', 'AAG'],
                  'V' : ['GUU', 'GUC', 'GUA', 'GUG'],
                  'A' : ['GCU', 'GCC', 'GCA', 'GCG'],
                  'D' : ['GAU', 'GAC'],
                  'E' : ['GAA', 'GAG'],
                  'G' : ['GGU', 'GGC', 'GGA', 'GGG']}
    proteinSeq = []
    with open(dataset) as dataset:
        RNASeq = dataset.read().strip()
        for i in range(0, len(RNASeq), 3):
            proteinSeq += [protein for protein,codon in codonTable.items() if RNASeq[i:i+3] in codon]
    return "".join(protein for protein in proteinSeq)

if __name__ == '__main__':
    print(TranslatingRNAIntoProtein("rosalind_prot.txt"))
