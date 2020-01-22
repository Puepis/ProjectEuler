
'''Description: PEuler 30 - Digit fifth powers

   Q: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

   See: https://projecteuler.net/problem=30

   Date: August 26, 2019
'''

def main():
    num_list = []
    max_sum = 6 * 9**5
    for x in range(2, max_sum):
        if x == get_digit_power_sum(x):
            num_list.append(x)
    print(sum(num_list))

def get_digit_power_sum(num):
    return sum([int(digit)**5 for digit in str(num)])

main()
