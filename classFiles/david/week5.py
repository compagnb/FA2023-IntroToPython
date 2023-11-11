# Week 5: Conditionals

## We can't concatenate (add) string and int
##
## Masking Varibles
## in order to masak a varible as a different type;
## we type the data type and put paraenthesis around the varible
ten = "10"
int(ten) #makes ten think its an integer

nine = 9 #makes nine think its a string

import random #imports a module for us to use other peoples code!

def testNumbers(guess, answer):
    if guess>answer:
        print(guess + "The number is lower than the number I am thinking of.")
    elif guess<answer:
        print( guess +"The number is higher than the number I am thinking of.")
    else:
        print("You guessed " + guess + " and I was thinking of " + answer + ". You win!")

#testNumbers(str(5), str(5))

#Start Game Here!
lowLimit = 1
highLimit = 100
ans = random.randint(lowLimit,highLimit)
##print(ans)
guess = input("I am thinking of a number between " + str(lowLimit) + " and " + str(highLimit) + ". What number am I thinking of?")
while int(guess) == ans:
    testNumber(int(guess),ans)
    guess = input("I am thinking of a number between " + str(lowLimit) + " and " + str(highLimit) + ". What number am I thinking of?")
print("You guessed " + guess + " and I was thinking of " + str(ans) + "You win!") 














    









  
    
