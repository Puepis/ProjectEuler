
'''Description: PEuler 16

   "What is the sum of the digits of the number 2^1000?"

   See: calcSum() function for reduce() demonstration and
   https://docs.python.org/release/2.7/tutorial/datastructures.html#functional-programming-tools
   -- 5.1.3 -- for details

   See: above link for map() explanation and altSolution() function for
   demonstration

   Date: Jan. 20, 2019
'''

import math

def main():

    # Calculate exponent
    num = int(math.pow(2, 1000))
    print(num)

    # Get digits
    digitList = getDigits(num)

    # ALTERNATIVE SOLUTION
    print altSolution(num)

    # Non built-in sum function
    #print calcSum(digitList)

def getDigits(num):
        
    digitList = []

    # Iterate through every digit of the number
    for index in range(len(str(num))):
        digitList.append(int(str(num)[index]))
    return digitList

def calcSum(digitList):

    # Two arguments - lambda function, iterative sequence (e.g. list)
    return reduce(lambda a, b: a + b, digitList)

def altSolution(num):

    # map() built-in function explanation
    # 1. Converts number to iterative data structure (str)
    # 2. Iterates through all digits in string and converts each to int
    # 3. Puts all digits in a list
    return sum(map(int, str(num)))

main()
