#todays lesson: input, graphics and shapes
import turtle
import random

randomNum = random.randint(0,10)

chibiTortomon = turtle.Turtle()
chibiTortomon.shape("turtle")
chibiTortomon.color("blue")
chibiTortomon.penup()
chibiTortomon.goto(100,100)
chibiTortomon.forward(-100)
chibiTortomon.right(90)
chibiTortomon.left(90)


Shoutmon = turtle.Turtle()
Shoutmon.color("red")
Shoutmon.penup()
Shoutmon.left(90)
Shoutmon.forward(85)
chibiTortomon.right(90)
for i in range(0,8):
    chibiTortomon.right(90)
    chibiTortomon.left(90)
    chibiTortomon.right(90)
    chibiTortomon.left(90)
    Shoutmon.right(90)
    Shoutmon.left(90)
    Shoutmon.right(90)
    Shoutmon.left(90)
    print("I love you!")
    print("Me too!")
    print("Bye!")
    for i in range(0,8):
        chibiTortomon.forward(50)
        chibiTortomon.right(45)
        if i%2 == 0:
            chibiTortomon.pendown()
        else:
              chibiTortomon.penup()
    print("Hey! It's you again!")
    chibiTortomon.right(90)
    chibiTortomon.left(90)
    chibiTortomon.right(90)
    chibiTortomon.left(90)
    Shoutmon.right(90)
    Shoutmon.left(90)
    Shoutmon.right(90)
    Shoutmon.left(90)
print("Let's talk turkey! Now how the heck do we find Mikey?")
print("Mikey's missing?")
print("NOOOOOO!!!")
chibiTortomon.right(90)
chibiTortomon.left(90)
chibiTortomon.right(90)
chibiTortomon.left(90)
Shoutmon.right(90)
Shoutmon.left(90)
Shoutmon.right(90)
Shoutmon.left(90)

