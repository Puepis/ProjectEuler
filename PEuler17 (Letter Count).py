
'''Description: PEuler 17

   "If all the numbers from 1 to 1000 (one thousand) inclusive were written out
   in words, how many letters would be used?"

   Date: Jan. 27, 2019
'''

# Define constants
UNIQUES = [0, len("one"), len("two"), len("three"), len("four"), len("five"), \
               len("six"), len("seven"), len("eight"), len("nine"), len("ten"), \
               len("eleven"), len("twelve"), len("thirteen"), len("fourteen"), \
               len("fifteen"), len("sixteen"), len("seventeen"), len("eighteen"), \
               len("nineteen")]
TENS = [len("twenty"), len("thirty"), len("forty"), len("fifty"), len("sixty"), \
        len("seventy"), len("eighty"), len("ninety")]

def main():

    numList = []

    # From zero to nineteen
    numList.extend(UNIQUES)

    # From twenty to ninety nine
    numList.extend(generateTens())

    # From 100 to 999
    numList.extend(generateHundreds(numList))

    # 1000
    numList.append(len("onethousand"))

    # Display total number of letters
    print sum(numList)

def generateTens():

    tensList = []

    for tens in TENS:

        # twenty, thirty,....ninety
        tensList.append(tens)

        # one, two,...nine
        for ones in range(1, 10):

            # twenty one, twenty two, etc.
            letters = tens + UNIQUES[ones]
            tensList.append(letters)

    return tensList

def generateHundreds(unitsList):

    hundredsList = []
    hunds1 = len("hundred")
    hunds2 = len("hundredand")

    for ones in range(1,10):

        # one hundred, two hundred,...nine hundred
        onesLetter = UNIQUES[ones]
        hundredsList.append(onesLetter + hunds1)

        # one, two,... ninety nine
        for units in range(1,100):

            # one hundred and one,.....nine hundred and ninety nine
            unitsLetter = unitsList[units]
            letters = onesLetter + hunds2 + unitsLetter
            hundredsList.append(letters)

    return hundredsList

main()
