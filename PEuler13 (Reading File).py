
'''Description: PEuler 13
   
   "Work out the first ten digits of the sum of the following 
   one-hundred 50-digit numbers." (numbers read from text file)
   
   Date: Jan. 20, 2019
'''

def main():
    
    # Open file
    numbersFile = open("numbers.txt", "r")
    
    # Initialize sum
    theSum = 0
    
    # Generate list of integers
    numbersList = numbersFile.readlines()
    for index in range(len(numbersList)):
        numbersList[index] = int(numbersList[index].strip())
    
    # Find sum
    for num in numbersList:
        theSum += int(num)
    
    # Display sum
    print theSum
    
    # Close file 
    numbersFile.close()
    
main()