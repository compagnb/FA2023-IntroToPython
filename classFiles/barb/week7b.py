#Week 7b
import turtle
import random

grinches=[]
vel=random.randint(1,5)
numOfGrinches=10

for i in range(0,numOfGrinches):
    grinches.append(turtle.Turtle())
    grinches[i].color("green")
    grinches[i].penup()
    grinches[i].speed()
    grinches[i].goto(random.randint(-300,300), random.randint(-300,300))
    grinches[i].setheading(random.randint(0,360))


