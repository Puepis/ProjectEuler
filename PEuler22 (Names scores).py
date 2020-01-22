
'''Description: PEuler 21 - Amicable Numbers

   Q: What is the total of all the name scores in the file?

   See: "p022_names.txt"
   See: https://projecteuler.net/problem=22

   Date: August 25, 2019
'''

def main():

    # Open file
    names_file = open("p022_names.txt", "r")
    names = [name.strip("\"") for name in names_file.read().split(',')]

    names.sort()

    # Process names
    alpha_values = []
    for name in names:
        alpha_value_total = 0

        # Calculate alphabetical value
        for letter in name:
            alpha_value = ord(letter) - 64
            alpha_value_total += alpha_value

        # Position value
        alpha_position = names.index(name) + 1
        alpha_score = alpha_position * alpha_value_total

        # Score list for all names
        alpha_values.append(alpha_score)

    print(sum(alpha_values))

main()
