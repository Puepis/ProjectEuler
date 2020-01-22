
'''Description: PEuler 27 - Quadratic Primes

   Q: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

   See: https://projecteuler.net/problem=27

   Date: August 26, 2019
'''
import math

def main():
    primes = sieve(1000)
    max_n = 0
    max_prod = 0
    n = 0
    for b in primes:
        for a in range(-999, 1000, 2):
            if b == 2:
                a -= 1
            n = count_consecutive_primes(a, b, set(primes))
            if n > max_n:
                max_n = n
                max_prod = a * b
    print(max_prod)

def count_consecutive_primes(a, b, primes):
    n = 0
    while True:
        y = f(n, a, b)
        if y in primes:
            n += 1
        else:
            break
    return n

def f(n, a, b):
    return (n*n + (a*n) + b)

def sieve(max):
    num_list = [x for x in range(max)]
    num_list[1] = 0

    for num in range(2, int(math.sqrt(max) + 1)):
        if num_list[num] != 0:
            for multiple in range(num**2, max, num):
                num_list[multiple] = 0

    prime_list = [x for x in num_list if x != 0]
    return prime_list
main()
