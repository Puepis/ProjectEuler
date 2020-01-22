
'''Description: PEuler 21 - Amicable amicable_numbers

   Q: Evaluate the sum of all the amicable numbers under 10000.

   See: https://projecteuler.net/problem=21
   Features: Generating divisors algorithm

   Date: August 25, 2019
'''

import math

def main():

    amicable_numbers = []
    for a in range(10000):
        b = d(a)
        if d(b) ==  a and a != b and a not in amicable_numbers:
            amicable_numbers.append(a)
            amicable_numbers.append(b)

    print(sum(amicable_numbers))

def d(n):
    divisor_sum = sum(generate_proper_divisors(n))
    return divisor_sum

def generate_proper_divisors(n):
    divisors = []

    # Up to sqrt(n)
    for num in range(1, int(math.sqrt(n) + 1)):

        # Divisible
        if n % num == 0:
            divisors.append(num)
            if num * num != n and num != 1:
                divisors.append(n // num)

    divisors.sort()
    return divisors

main()
