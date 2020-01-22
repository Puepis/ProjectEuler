
'''Description: Finding Largest Palindrome from Product of Two Three-Digit 
   Numbers
'''

def main():
    # Range
    minRange = input("Enter min range: ")
    maxRange = input("Enter max range: ")
    palindrome = checkPalindrome(minRange, maxRange)
    
    # Output
    print "The largest palindrome is " + str(palindrome)
    
def checkPalindrome(rmin, rmax):
    palindromeList = []
    
    # Nested Loops
    for n in range(rmin, rmax+1):
        for x in range(n, rmax+1):
            product = n*x
            
            # Create digit list
            digitList = [digit for digit in str(product)]  
            
            # Check if palindrome
            if digitList[:3] == digitList[:2:-1]:
                palindromeList.append(product)
                print product
    if palindromeList:
        return max(palindromeList) 
main()
            