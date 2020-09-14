def MendelsFirstLaw(dataset):
    """Determine the probability of of a dominant allele individual from two randomly selected mating organisms"""
    
    matingProb = {"k*k": 1,
                   "k*m": 1,
                   "m*k": 1,
                   "k*n": 1,
                   "n*k": 1,
                   "m*m": 0.75,
                   "m*n": 0.5,
                   "n*m": 0.5,
                   "n*n": 0}
    domAlleleProb = 0
    with open(dataset) as dataset:
        organisms = ['k','m','n']
        organismPop = dict(zip(organisms, dataset.read().split()))
        totalPop = sum([int(pop) for pop in organismPop.values()])
        for organism, population in organismPop.items():
            organismProb = int(organismPop.get(organism)) / totalPop
            for matingOrganism in organisms:
                matingTotalPop = totalPop - 1
                matingOrganismPop = int(organismPop.get(matingOrganism)) if matingOrganism != organism else int(organismPop.get(matingOrganism)) -1
                matingOrganismProb = matingOrganismPop / matingTotalPop
                domAlleleProb += matingProb.get(organism + "*" + matingOrganism) * (organismProb * matingOrganismProb) 
    return domAlleleProb 
if __name__ == '__main__':
    print(MendelsFirstLaw("rosalind_iprb.txt"))
