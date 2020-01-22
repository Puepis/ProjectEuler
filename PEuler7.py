
'''Description: Determine 10 0001st prime number (inefficient - check PEuler10
   for more efficient algorithm)'''

import math

primeList = [2,3,5,7,11,13,17,19]

def main():
    
    num = 21
    while len(primeList) < 10001:
        # add all new prime numbers to primeList
        if isPrime(num):
            primeList.append(num)
        num += 2
    print primeList[10000]

def isPrime(num):
    isPrime = True
    for n in primeList:
        if n <= math.sqrt(num):
            if num % n == 0:
                isPrime = False
                break
    return isPrime


    
main()
        
            
        
    