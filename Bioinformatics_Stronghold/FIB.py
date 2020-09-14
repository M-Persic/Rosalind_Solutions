def RabbitsAndRecurrenceRelations(dataset):
    """Return the total number of rabbit pairs present after a given amount of months using the Fibonacci formula"""

    totalPairs, nonMaturePairs, maturePairs = 0, 0, 1
    with open(dataset) as dataset:
        data = dataset.read().strip()
        months = int(data.split()[0])
        pairs = int(data.split()[1])
        for month in range(1, months):
            totalPairs = nonMaturePairs + maturePairs
            newNonMaturePairs = pairs * maturePairs
            maturePairs += nonMaturePairs
            nonMaturePairs = newNonMaturePairs
    return totalPairs
    
if __name__ == '__main__':
    print(RabbitsAndRecurrenceRelations("rosalind_fib.txt"))
