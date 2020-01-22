
'''Description: PEuler 18 - Maximum path sum I

   Q: Find the maximum total from top to bottom of the triangle below:
   (see max_path_sum_1_triangle.txt)

   Explanation: Check maximum sum from bottom-up using a grid. This solution
   also works for problem 67 - Maximum path sum II

   See: "max_path_sum_1_triangle.txt"
   See: "p067_triangle.txt"
   See: https://projecteuler.net/problem=18

   Date: August 25, 2019
'''
import time

def main():

    start_time = time.time()

    triangle_file = open("p067_triangle.txt", "r")

    triangle_lines = triangle_file.readlines()
    num_lines = len(triangle_lines)

    # Create grid
    grid = []
    for line in triangle_lines:
        row = []
        line = line.strip().split()
        for num in line:
            row.append(int(num))
        if len(row) < num_lines:
            row += [0 for i in range(num_lines - len(row))]
        grid.append(row)

    # Start from second last line and move up
    start_index = num_lines - 2
    for row in range(start_index, -1, -1):
        #print("ROW: " + str(row))
        for col in range(row + 1):

            # Compare the two numbers below and add the higher one
            num_south = grid[row + 1][col]
            num_south_east = grid[row + 1][col + 1]

            grid[row][col] += max(num_south, num_south_east)
        grid.remove(grid[row + 1])
        #display_grid(grid)

    print("Maximum sum: " + str(grid[0][0]))
    print("Time: %.3f ms" % ((time.time() - start_time) * 1000))

def display_grid(grid):
    for row in grid:
        print(row)

main()
