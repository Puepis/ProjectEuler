
'''Description: Prime Factor any Number
   
   Date: Sep. 2018
   
   v1. Just Factoring - Displays all factors one by one in huge list
   v2. Utilised Counter() datatype object to simplify program for readibility
   v3. Implemented execution time display 
   '''

import math
from collections import Counter
import time

def primeFactorization(x):
    
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

def simplify(factorList):
    '''Simplify the comprehensive list of factors.'''
    
    # Create counter object (dictionary subclass)
    count = Counter()
    
    # Count num of occurrences for each factor
    for factor in factorList:
        count[factor] += 1
    
    # Turn counter object into list of tuples
    count = count.items()
    
    # Change formatting
    for index in range(len(count)):
        count[index] = str(count[index][0]) + "^" + str(count[index][1])
        
    return count
        

def main():
    
    num = input("Enter the number: ")
    
    # Start time
    start_time = time.time()
    factors = primeFactorization(num)
    factors = simplify(factors)
    print "The prime factors of ", num, "are " + str(factors) + "."
    
    # Display execution time
    print("--- %s seconds to calculate ---" % (time.time() - start_time))

main()
        