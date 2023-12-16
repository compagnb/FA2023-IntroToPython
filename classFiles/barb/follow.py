import turtle

t=turtle.Turtle('turtle')
t.penup()

def get_coor(x, y):
    print(x, y)

while True:
    t.goto(get_coor)
    
