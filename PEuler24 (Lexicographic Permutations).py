
'''Description: PEuler 24 - Lexicographic Permutations

   Q: What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

   See: https://projecteuler.net/problem=24

   Date: August 25, 2019
'''
import itertools

def main():

    permutations = list(itertools.permutations(range(10)))

    count = 0
    for tup in permutations:
        count += 1
        if count == 1000000:
            num = ''.join(map(str,(tup)))
            print(num)
            break
main()
