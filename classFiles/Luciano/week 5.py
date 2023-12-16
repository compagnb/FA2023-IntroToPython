# Week 5: Conditionals

##We can't add strings and ints 
##
##Masking Varibles 
##in order to mask a varible as as different type the data and put paraenthasis around the varible
##we type te data type and put paraenthesis around the varible
ten = "10"
int(ten) #makes ten think its an integer 

nine = 9
str(nine)#makes nine think its a string

import random #import a module for us to use other peoples code! 

def testNumbers(guess, answer):
    if guess>answer:
        print(guess +" is lower than the number I am thinking of.")
     guess<answer
     print("is higher than the number I was thinking of")
    else:
        print("You guessed" + guess + " and I was thinking of " + answer + ". You win!")  

#testNumbers(str5), str(5))

#start Game Here!
lowLimit = 1
highLimitn = 100
ans = random.randit(1,000)
#print(ans)
guess = input("I am thinking of a number between" + str(lowLimit) + "and" + str(highLimit) + ".What number am I thing of?"
while guessed == ans:
    testNumber(int(guess),ans)


