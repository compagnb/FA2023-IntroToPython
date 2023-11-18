# Week 5: Conditionals

## We can't concatenate (add) strings and ints
##
## Masking Variables
## in order to mask a variable as a different type;
## we type the data type and put paraenthesis around the variable
ten = "10"
int(ten) #makes ten think its an integer

nine = 9
str(nine)#makes nine think its a string

import random #imports a module for us to use other peoples code!

def testNumbers(guess, answer):
    if guess < answer:
        print(str(guess) + " is lower than the number I am thinking of.")
    elif guess > answer:
        print(str(guess) + " is higher than the number I am thinking of.")
  
      
testNumbers(str(50), str(5))

#Start Game Here!
lowLimit = 1
highLimit = 100
ans = random.randint(lowLimit,highLimit)
#print(ans)
guess = input("I am thinking of a number between " + str(lowLimit) + " and " + str(highLimit) + ". What number am I thinking of?")

while int(guess) != ans:
    testNumbers(int(guess), ans)
    guess = input("I am thinking of a number between " + str(lowLimit) + " and " + str(highLimit) + ". What number am I thinking of?")

print("You guessed " + guess + " and I was thinking of " + str(ans) + ". You win!")





