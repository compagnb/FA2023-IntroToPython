#Week 7b
import turtle
import random

grinches=[]
vel=random.randint(1,5)
numOfGrinches=70

for i in range(0,numOfGrinches):
    grinches.append(turtle.Turtle())
    grinches[i].color("green")
    grinches[i].penup()
    grinches[i].speed()
    grinches[i].goto(random.randint(-500,500), randint(-500,500))
    gricnhes[i].setheading(random.randint(0,360))

while True:
