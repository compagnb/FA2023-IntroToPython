#Todays lesson: input, graphics & shapes!
import turtle
import random

randomNum = random.randint(0,10)

mike = turtle.Turtle()
mike.shape("turtle")
mike.color("orange")
mike.speed(0)
leo.shape("turtle")
leo.color("blue")
#mike.penup() #removes the trail that mike leaves
#mike.left(90) #rotates mike 90 left
#mike.goto(100,100) #moves mike to 100,100
#mike.forward(100) #moves mike foward 100 pixels
#mike.right(90) #rotates mike 90 degress right
#mike.backward(200) # moves mike bacward 200 pixels
#mike.penup() #turns on the trail on

#make a shape

for i in range(1,19):
 mike.forward(50)
 #mike.right(45)
 if i%2 == 0:# checks if there is a remainder when divided by 2
    mike.left(175)
##      leo.lefrt(175)
##      leo.pendown()
 else:
    mike.left(225)
      #mike.penup()
    leo.right(155)
    
