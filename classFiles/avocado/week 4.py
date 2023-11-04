# today's lesson:conditionals!!!

def testHigher (theNum, guessNum):
     if theNum > guessNum:
         print("The number is higher than your guess.")

def testLower (theNum, guessNum):
     if theNum < guessNum:
         print("The number is lower than your guess.")

def testEquals (theNum, guessNum):
     if theNum==guessNum:
         print("Good job! you chose the right number!")
         guessCorrect = True
#testHigher(3, 2)
#testLower(3, 4)
#testEquals(3, 3)

## game play starts here
guessCorrect = False
number=8
#str(8)
while guessCorrect == False:
    guess = input("I'm thinking of a number between 1 and 10, guess the number.")
    testHigher(number, int(guess))
    testLower(number, int(guess))
    testEquals(number, int(guess))
    
