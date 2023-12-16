import turtle




def changeTurtle(t, tColor, tShape):
    t.color(tColor)
    t.shape(tShape)

wn = turtle.Screen()
img = "invader.gif"
wn.register_shape(img)
invader = turtle.Turtle()
changeTurtle(saucer, "black", img)
