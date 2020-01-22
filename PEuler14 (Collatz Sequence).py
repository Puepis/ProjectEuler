
'''Description: PEuler 14

   "Which starting number, under one million, produces the longest collatz
   chain?"

   Collatz Conjecture: Prove that for all positive integers, a complete collatz
   sequence ends (sequence only ends when 1 is reached).

   See: Collatz() function for sequence definition.

   Date: Jan. 20, 2019
'''

import math

def main():
    '''Find the number that produces the largest collatz sequence within a
    certain range.'''

    greatestLen = 0
    for x in range(500001, 1000000, 2):
        length = generateCollatzSequence(x)
        if length > greatestLen:
            greatestLen = length
            num = x

    print "The greatest length of", greatestLen, "is produced by", num

def generateCollatzSequence(start):
    '''Generates a collatz sequence iteratively.'''

    sequence = []
    num = start
    done = False

    # Conditional loop
    while not done:


        sequence.append(num)

        # Sequence ends when 1 is reached
        if num == 1:
            length = len(sequence)
            done = True
        else:
            num = Collatz(num)

    return length

def Collatz(num):
    '''Rule: Next number in sequence is (n/2) if n is even, (3n + 1)
    if n is odd.'''

    # Collatz Rule

    if num % 2 == 0:
        num /= 2
    else:
        num = 1 + (3 * num)

    return num

main()
