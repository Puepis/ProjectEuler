
'''Description: PEuler 31 - Coin sums

   Q: How many different ways can £2 be made using any number of coins?

   See: https://projecteuler.net/problem=31
   See: https://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/ for Dynamic Programming explanation.

   Date: August 26, 2019
'''

def main():
    coins = 200
    coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

    # Number of ways to make [x] amount
    combinations = [0 for x in range(coins + 1)]

    # Base value - there is 1 way to make 0p
    combinations[0] = 1

    # Every coin value
    for coin_value in coin_values:

        # Start at coin value and move up
        for x in range(coin_value, coins + 1):

            # Add ways by subtracting coin value and the remaining index
            combinations[x] += combinations[x - coin_value]

    print("There are " + str(combinations[-1]) + " ways of generating " + str(coins) + "p.")



main()
