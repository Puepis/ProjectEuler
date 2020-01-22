

'''Description: Largest product in a series (1000 digit number)

   Date: September 23, 2018'''

def main():
    
    num = input("Enter number: ")
    digitList = [int(digit) for digit in str(num)]
    digitList = removeZeroProducts(digitList)
    largestProduct = findLargestProduct(digitList)
    print largestProduct
    
def removeZeroProducts(digits):
    numberList = []
    for nmin in range(0, 988):
        isZero = False
        # Check if any of the digits are 0, product would equal 0
        for digit in digits[nmin:nmin+13]:
            if digit == 0:
                isZero = True
        # Add to number list if number doesn't contain 0
        if isZero == False:
            numberList.append(digits[nmin:nmin+13])
    return numberList
        
def findLargestProduct(digits):
    # Get largest product out of all the numbers in 2D list 
    productList = []
    for item in digits:
        product = findProduct(item)
        productList.append(product)
    return max(productList)

def findProduct(numList):
    # Find the product of all the numbers in a list 
    product = 1
    for digit in numList:
        product *= digit
    return product

main()
        
    
    