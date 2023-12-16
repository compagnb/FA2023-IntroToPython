#Week

import turtle

vel=3

grinch = turtle.Turtle()
grinch.color("green")
grinch.penup()
grinch.speed(0)

while True:
    grinch.forward(ve1)
    if grinch.xcor()>300 or grinch.xcor()<-300:
        grinch.left(30)
    if grinch.ycor()>300 or  grinch.ycor()<-300:
        grinch.left(30)
