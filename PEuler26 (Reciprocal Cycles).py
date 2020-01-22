
'''Description: PEuler 26 - Reciprocal Cycles

   Q: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

   See: https://projecteuler.net/problem=26
   See: https://www.xarg.org/puzzle/project-euler/problem-26/ for math explanation

   Date: August 26, 2019
'''
import math

def main():
    primes = sieve(1000)

    # Cycle through primes to find max length
    max = 0
    d = 0
    for prime in primes:
        cycle = get_cycle_length(prime)
        if cycle > max:
            max = cycle
            d = prime
    print(d)

# Reciprocal cycle length using modulo
def get_cycle_length(num):
    a, n = 10, 0
    r = 0
    while r != 1:
        n += 1
        r = (a ** n) % num
    return n

# Generate prime numbers (excluding 2, 3, 5)
def sieve(max):
    num_list = [x for x in range(max)]
    num_list[1] = 0

    for num in range(2, int(math.sqrt(max) + 1)):
        if num_list[num] != 0:
            for multiple in range(num**2, max, num):
                num_list[multiple] = 0

    prime_list = [x for x in num_list if x != 0 and x != 2 and x != 3 and x != 5]
    return prime_list
main()
