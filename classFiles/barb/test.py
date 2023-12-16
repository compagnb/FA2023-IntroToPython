import turtle

rudolphImg = "rudy.gif"
turtle.register_shape(rudolphImg)

wn = turtle.Screen() # Create screen
rudolph = turtle.Turtle() # Create turtle
rudolph.shape(rudolphImg)
rudolph.penup()

reindeer = turtle.Turtle()
reindeer.penup()



def drag(x, y): # Define drag function
    rudolph.ondrag(0)
    reindeer.goto(rudolph.xcor()+10, rudolph.ycor()+10)
    rudolph.setheading(rudolph.towards(x, y))
    rudolph.goto(x, y)
    rudolph.ondrag(drag)

    
    
    

rudolph.ondrag(drag) # Use function on turtle
turtle.mainloop()




##import turtle
##
##def move_turtle(x, y):
##    turtle.setpos(x, y)
##
##turtle.onscreenclick(move_turtle)

turtle.mainloop()
