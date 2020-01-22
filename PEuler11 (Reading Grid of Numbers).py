
'''Description: PEuler 13
   
   "Work out the first ten digits of the sum of the following 
   one-hundred 50-digit numbers." (numbers read from text file)
   
   Date: Jan. 20, 2019
'''

from operator import mul

def main():
    
    # Open file
    gridFile = open("grid.txt", "r")
    
    # Initialize sum
    theSum = 0
    numbersList = []
    
    # Convert grid to list of integers
    for line in gridFile:
        line = line.split()
        for index in range(len(line)):
            line[index] = int(line[index])
        numbersList.append(line)
    
    #numbersList = reduceNumbers(numbersList)
    horiz = checkHorizProd(numbersList)
    vert = checkVertProd(numbersList)
    diag = checkDiagProd(numbersList)
    
    # Display greatest products
    print horiz
    print vert
    print diag

    # Close file 
    gridFile.close()

def checkHorizProd(numList):
    
    # Check greatest horizontal product
    product = 0
    for x in range(len(numList)):
        
        # Iterate to 4th last column
        for y in range(len(numList[x]) - 3):
            
            # Find product of sliced list
            currentProd = reduce(mul, numList[x][y:y+4])
            
            # Replace greater product
            if currentProd > product:
                product = currentProd         
                
    return product
            

def checkVertProd(numList):
    
    # Find greatest vertical product
    product = 0
    
    # Iterate to 4th last row
    for x in range(len(numList) - 3):
        for y in range(len(numList[x])):
            
            # Vertical product
            currentProd = numList[x][y] * numList[x+1][y] * numList[x+2][y] * numList[x+3][y]
            if currentProd > product:
                product = currentProd
    return product

def checkDiagProd(numList):
    
    product = 0
    
    # Bottom right
    for x in range(len(numList) - 3):
        for y in range(len(numList[x]) - 3):
            currentProd = numList[x][y] * numList[x+1][y+1] * numList[x+2][y+2] * numList[x+3][y+3]
            if currentProd > product:
                product = currentProd
    
    # Bottom left
    for x in range(len(numList) - 3):
        for y in range(len(numList) - 1, 2, -1):
            currentProd = numList[x][y] * numList[x+1][y-1] * numList[x+2][y-2] * numList[x+3][y-3]
            if currentProd > product:
                product = currentProd
                
    return product

main()