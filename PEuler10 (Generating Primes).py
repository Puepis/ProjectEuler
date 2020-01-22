
'''Generating prime numbers using Sieve of Eratosthenes algorithm and
   summation of the primes.

   Date: September 26, 2018'''


import math

# Obtain max limit (e.g. 200 indicates all prime numbers below 200)
listSize = int(input("Enter upper range: "))

# Generate a list of n values from 0 to n-1
numList = [num for num in range(listSize)]

# Set second value in the list to 0 - indicating non-prime
numList[1] = 0

# Sift through multiples of 2 to root(n) - 0 value indicates non-prime
for num in range(2, int(math.sqrt(listSize) + 1)):

    # If the number is prime
    if numList[num] != 0:

        # Change all multiples of num starting from num^2 and incrementing
        # by multiples of num
        for multiple in range(num**2, listSize, num):
            numList[multiple] = 0

# Display sum of all the primes below listSize
print(numList)
