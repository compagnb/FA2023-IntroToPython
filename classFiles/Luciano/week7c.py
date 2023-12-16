#Week 7b
import turtle
import random

grinchImg="grinch.gif"
turtle.register_shape(grinchImg)

maxImg="max walking .gif"
turtle.register_shape(maxImg)

bgpicture="mountain grinch.gif"

window=turtle.Screen()
window.bgcolor("black")
window.title("Gricnhes Walking")
window.bgpic(bgpicture) 

grinches=[]
vel = random.randint(1,5)
numOfGrinches = 10

for count in range(0,numOfGrinches):
    grinches.append(turtle.Turtle())
    grinches[count].shape(grinchImg)
    grinches[count].color ("green")
    grinches[count].penup()
    grinches[count].speed(0)
    grinches[count].goto(random.randint(-300,300),random.randint(-300,300))
    grinches[count].setheading(random.randint(0,360))

    while True:
       for grinch in grinches:
           grinch.forward(vel)
