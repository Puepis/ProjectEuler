
'''Description: Difference between sum of the squares of the first n
   natural numbers and the square of the sum.'''

def main():
    num = input("Enter num: ")
    sumOfSquares = getSumOfSquares(num)
    squareOfSum = getSquareOfSum(num)
    print squareOfSum - sumOfSquares
    
def getSumOfSquares(num):
    theSum = 0
    for n in range(1, num+1):
        theSum += n**2
    return theSum

def getSquareOfSum(num):
    squareOfSum = ((num*(num+1))/2)**2
    return squareOfSum
    
main()
        