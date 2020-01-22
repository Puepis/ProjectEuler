
'''Description: PEuler 12 "Find first triangle number to have 
   over five hundred divisors." 
   
   Utilizes prime factorization and Counter() class, as demonstrated in 
   PEuler 3. 
   
   Date: Jan. 20, 2019
'''

import math
from collections import Counter

def main():

    # Number list
    triNums = []

    prevSum = 0
    x = 1

    # nth triangular number
    upperRange = 20

    # Generate Triangular Number List
    while True:
        newSum = prevSum + x
        triNums.append(newSum)
    
        #print findNumDivisors(newSum)
        # Find number of divisors
        if findNumDivisors(newSum) >= 500:
            break
        
        prevSum = triNums[x-1]
        x += 1
        
    print triNums[len(triNums) - 1]

def primeFactor(x):
    
    factors = []
    origNum = x 
    num = origNum
    
    # Factor out multiples of 2
    while num % 2 == 0:
        num /= 2
        factors.append(2)
     
     # Test all odd numbers from 3 to sqrt(original number)
    for n in range(3, int(math.sqrt(origNum)) + 1, 2):
        while num % n == 0:
            num/= n
            factors.append(n)
            
    # If remaining term is > 1, the term itself must be prime
    if num > 1:
        factors.append(num)
        
    return factors

def findNumDivisors(num):
    '''Simplify the comprehensive list of factors.'''
    
    numDivisors = 1
    factorList = primeFactor(num)
    
    # Create counter object (dictionary subclass)
    count = Counter()
    
    # Count num of occurrences for each factor
    for factor in factorList:
        count[factor] += 1
    
    # Turn counter object into list of tuples
    count = count.items()
    
    # Change formatting
    for index in range(len(count)):
        numDivisors *= (count[index][1] + 1)
        
    return numDivisors

main()
    
    
    
    