#Week 7

import turtle

grinch = turtle.Turtle()
grinch.color("green")
grinch.penup()
grinch.speed()

vel=100

while True:
    grinch.forward(vel)
    if grinch.xcor()>300 or grinch.xcor()<-300:
        grinch.left(180)
    if grinch.ycor()>300 or grinch.ycor()<-300:
        grinch.left(30)
        if grinch.xcor()>300 or grinch.xcor()<-300:
        grinch.left(180)
    if grinch.ycor()>300 or grinch.ycor()<-300:
        grinch.left(30)
