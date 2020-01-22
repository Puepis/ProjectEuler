
'''Description: PEuler 25 - 1000-digit Fibonacci Number

   Q: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

   See: https://projecteuler.net/problem=25

   Date: August 25, 2019
'''

def main():
    fibonacci_list = [0, 1]
    index = 0
    while True:
        next = sum(fibonacci_list[-2:])
        fibonacci_list.append(next)
        if len(str(next)) == 8:
            index = len(fibonacci_list) - 1
            break;
    print(index)
main()
