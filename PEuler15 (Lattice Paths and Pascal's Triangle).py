
'''Description: PEuler 15

   "How many routes are there through a 20�20 grid? (only restricted to right
   and down movements)"

   Lattice Paths -- Shortest Path Diagrams

   The number of possible paths of length 2n from a corner of an
   n-by-n grid to the opposite corner (central binomial coefficients - think
   Pascal's triangle)

   See: https://www.robertdickau.com/manhattan.html for explanation

   Date: Jan. 20, 2019
'''

import math

def main():

    gridSize = input("Enter the grid size: ")
    numPaths = getNumPaths(gridSize)
    print "The total number of paths for a " + str(gridSize) + " by " + \
          str(gridSize) + " grid is", numPaths

def getNumPaths(size):
    '''Number of paths equals (2n choose n) -- see above link for
    explanation.'''

    # Combinations
    paths = math.factorial(2 * size) / math.pow(math.factorial(size), 2)
    return int(paths)

main()
