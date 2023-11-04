

def testHigher (theNum, guessNum):
    if theNum > guessNum:
        print("The number is higher than your guess")

       
def testLower (theNum, guessNum):
    if theNum < guessNum:
        print("The number is Lower than your guess")
   
def testEquals (theNum, guessNum):
    if theNum == guessNum:
        print("That is correct!")
        guessCorrect = True
     
#testHigher(3, 2)
#testLower(3, 4)
#testEqual(3, 3)

## game play starts here
guessCorrect = False
number=11
#str(11)
while guessCorrect == False:
    guess = input("Im thinking of a number 1 and 14, guess the number.")
    testHigher(number, int(guess))
    testLower(number, int(guess))
    testEquals(number, int(guess))
    
