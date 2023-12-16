#today lesson input, graphics & shapes!
import turtle
import random

randomNum = random.randint(0,10)

mike = turtle.Turtle()
mike.shape("turtle")
mike.color("orange")
#basic Tu
#mike.penup()  #removes the trail that mike leaves 
#mike.left(90) #rotates mike 90 left
#mike.goto(100,100) #moves mike to 100,100
#mike.forward(100) #moves mike forward 100 pixels 
#mike.right(90) #rotates mike 90 degrees right
#mike.backward(200) #moves mike backward 200 pixels
#mike.pendown() #turns on teh trail on

#make a shape

for i in range(1,19):
    mike.forward(50)
    #mike.right (45)
    if i%2 ==0:
       mike.left(175)
       #mike.right(45)
       if i%2 == 0:
           mike.left(175)
           leo.left(175)
           leo.pendown()
       else:
           mike.left(225)
           leo.left(255)
           leo.penup()
           raph.left(175)
          raph.pendown()

          else: mik.left(225)
##                  leo.left(225)
##                  leo.penup ()
##                  raph.left(225)
##                  raph.left(225)
##                  raph.pendown()
          
