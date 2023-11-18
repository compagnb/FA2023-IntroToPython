#todays lesson: modulus, for loops!
import turtle
import random

randomNum = random.randint(0, 10)

mike = turtle.Turtle()
mike.shape("turtle")
mike.color("orange")
mike.speed(0)
leo = turtle.Turtle()
leo.shape("turtle")
leo.color("blue")
raph = turtle.Turtle()
raph.shape("turtle")
raph.color("red")
don = turtle.Turtle()
don.shape("turtle")
don.color("purple")
#basic turtle commands
#mike.penup() #removes the trail that mike leaves
#mike.left(90) #rotates mike 90 left
#mike.goto(100,100) #moves mike to 100, 100
#mike.forward(100) #moves mike forward 100 pixels
#mike.right(90) #rotates mike 90 degrees right
#mike.backward(200) #moves mike backward 200 pixels
#mike.pendown() #turns on the trail on

#make a shape

for i in range(1,19): #counting loop
    mike.forward(50*i)
##    leo.forward(100)
##    raph.forward(100)
##    don.forward(75)
    if i%2 == 0: #checks if there is a remainder when divided by 2
        mike.left(175)
##        leo.left(175)
##        leo.pendown()
##        raph.left(175)
##        raph.penup()
##        don.left(175)
    else:
        mike.left(225)
##        leo.left(255)
##        leo.penup()
##        raph.left(255)
##        raph.pendown()
##        don.left(225)
        









