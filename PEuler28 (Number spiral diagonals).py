
'''Description: PEuler 28 - Number spiral diagonals

   Q: What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?

   See: https://projecteuler.net/problem=28

   Date: August 26, 2019
'''
import time

def main():
    start = time.time()
    corners_list = [1]
    corners = 4
    grid_size = 1001
    for x in range(2, grid_size, 2):
        for y in range(corners):
            corners_list.append(corners_list[-1] + x)
    print(sum(corners_list))
    print("Time: %.3f ms" % ((time.time() - start) * 1000))

main()
