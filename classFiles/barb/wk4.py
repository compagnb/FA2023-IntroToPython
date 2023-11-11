# Today's lesson: Conditionals!!!
# Boolean is a data type that is only 1 or 0 (true or false)
# = sets a variable equal to a value
# == tests a if a value is equal to another

def testHigher(theNum, guessNum):
    if theNum > guessNum:
        print("The number is higher than your guess.")

def testLower(theNum, guessNum):
    if theNum < guessNum:
        print("The number is lower than your guess.")

def testEquals(theNum, guessNum, guessCorrect):
    
    if theNum == guessNum:
        print("Correct! You chose the right number")
        guessCorrect = True

#testHigher(3, 2)
#testLower(3, 4)
#testEquals(3, 3)

## game play starts here
guessCorrect = False
number=5
#str(5)
while guessCorrect == False:
    guess = input("I'm thinking of a number between 1 and 10, guess the number.")
    testHigher(number, int(guess))
    testLower(number, int(guess))
    testEquals(number, int(guess))










