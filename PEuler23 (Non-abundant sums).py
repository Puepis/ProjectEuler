
'''Description: PEuler 23 - Non-abundant sums

   Q: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

   See: https://projecteuler.net/problem=23

   Date: August 25, 2019
'''
import math
import time

def main():

    start_time = time.time()

    # Generate list of non-abundant-sum numbers
    num_list = []
    for num in range(1, 28123 + 1):
        if not is_abundant_sum(num):
            print(num)
            num_list.append(num)

    print(sum(num_list))
    print("Time: %.3f ms" % ((time.time() - start_time) * 1000))

def is_abundant_sum(n):

    # Set decreases computation time by A LOT
    abundants_set = set(abundants_list)

    # Check if number is the sum of two abundant numbers
    for x in abundants_list:
        if x > n:
            return False
        if (n - x) in abundants_set:
            return True
    return False

def is_abundant(n):
    return sum(generate_proper_divisors(n)) > n

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

if __name__ == '__main__':
    # Create list of abundant numbers
    abundants_list = [x for x in range(1, 28123 + 1) if is_abundant(x)]
    main()
