# Today's lesson: Conditionals!!!
# Boolean is a data type that is only equal to 1 and 0 (true or false)
# = sets a variable equal to a value
# == test a if a value is equal to another

def testHigher(theNum, guessNum):
    if (theNum > guessNum):
        print("The number is higher than your guess.")

        
def testLower(theNum, guessNum):
    if (theNum < guessNum):
        print("The number is lower than your guess.")

        
def testEquals(theNum, guessNum):
    if (theNum == guessNum):
        print("Correct! You chose the right number.")
        guessCorrect = True
        

#testHigher(3, 2)
#testLower(2,3)
#testEquals(3,3)

## game play starts here
guessCorrect = False
number=3

while guessCorrect == False:
    guess = input("I am thinking of a number between  1 and 10 guess the number.")
    testHigher(number, int(guess))
    testEquals(number, int(guess))
    testLower(number, int(guess))

   
