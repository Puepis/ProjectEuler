
'''Generating Pythagorean triples using Euclid's formula, using
   generated positive coprime pairs (two ternary trees).

   Date: September 23, 2018'''


def main():
    pythaList = []
    coprimeList = generatePrimCoPrimes()
    # Get a pythagorean triple for every coprime pair
    for pair in coprimeList:
        triples = generatePythaTriples(pair)
        pythaList.extend(triples)

    # List of triple that matches the 1000 sum
    matchedSum = checkSum(pythaList)
    if matchedSum:
        product = findProduct(matchedSum)
        print product
    else:
        print "None of the triples add up to 1000."

def generatePrimCoPrimes():
    # Start with two root nodes
    coprimeList = [[2,1],[3,1]]
    for pair in coprimeList:
        # Generate 3*10 pairs of primitive coprimes
        if coprimeList.index(pair) < 10:
            a,b,c = generateBranches(pair)
            coprimeList.append(a)
            coprimeList.append(b)
            coprimeList.append(c)
    return coprimeList

def generateBranches(pair):
    # Generate 3 branches per pair of coprimes (ternary tree)
    m,n = pair
    branchOne = [2*m - n, m]
    branchTwo = [2*m + n, m]
    branchThree = [m + 2*n, n]
    return branchOne, branchTwo, branchThree

def generatePythaTriples(pair):
    # Generate pythagorean triple using Euclid's formula
    tripletList = []
    m,n = pair
    a = (m + n)*(m - n)
    b = 2*m*n
    c = m**2 + n**2

    # Pythagorean triple
    triple = [a,b,c]

    # Multiples of primitive triple
    for k in range(1,30):
        tripletList.append([k*n for n in triple])
    return tripletList


def findProduct(numList):
    # Find the product of all the numbers in a list
    product = 1
    for digit in numList:
        product *= digit
    return product

def checkSum(tripleList):
    # Check if any triplet sums to 1000
    for triple in tripleList:
        if sum(triple) == 1000:
            return triple
main()
