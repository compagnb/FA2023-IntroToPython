#Todays's lesson: Condititionals!!!
#boolean is a data type that is only 1 or 0 (true or False) 
# = sets a variable is equal to a value
# == tests a if a value is equal to another 
def testHigher(theNum,  guessNum):
    if theNum > guessNum:
       print("the number is higher")

def testLower(theNum,  guessNum):
    if theNum < guessNum:
       print("the number is lower")

def testEquals(theNum,  guessNum):
    if theNum == guessNum:
       print("Correct! You chose the right number")
       guessCorrect = True

#testHigher(3,2)
#tetsLower(3,4)
#tetes equales (3,3)

## game play starts here
guessCorrect =False
number=5

while guessCorrect== False:
    guessNum = input("I'm thinking of a number between 1 and 10, guess the number.")
    testHigher(number, int(guess))
    testLower(number, int(guess))
    testsEquals(number, int(guess))
    










