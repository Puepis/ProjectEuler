
'''Description: PEuler 20 - Factorial Digit Sum

   Q: Find the sum of the digits in the number 100!

   Date: August 25, 2019
'''

import math

def main():

    num = math.factorial(n)

    # Digit sum
    print("The sum is:", sum(map(int, str(num))))

if __name__ == '__main__':
    n = 100
    main()
