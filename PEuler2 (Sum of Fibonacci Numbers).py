

'''Description: Get the sum of all even fibonacci numbers < 4000000

   Date: September 22, 2018'''

def theSum():
    myList = [0,1]
    prevSum = 0
    while True:
        prevSum = sum(myList[-2:])
        if prevSum < 4000000:
            myList.append(prevSum)
        elif prevSum > 4000000:
            break
    
    # Get all even terms
    evenList = [n for n in myList if n % 2 == 0]
    
    # Display sum
    totalSum = sum(evenList)
    print totalSum
    
theSum()