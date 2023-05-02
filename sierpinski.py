import turtle
import math
from random import randint

t = turtle.Turtle()
t.hideturtle()
size = 200
print("Drawing... please wait.")
turtle.tracer(False)

# draw 3 points as a shape of a triangle
# draw a point somewhere on one of the side of the triangle
# repeat this 2 step VVV
# choose one the 3 original points
# draw a point halfway from the point just drew to the original point choosen

def DrawPoint(x, y, heading):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.forward(1)
    t.penup()
    t.setheading(heading)

def gotoMiddle(destination):
    x = t.pos()[0] + ((destination[0] - t.pos()[0] ) / 2)
    y = t.pos()[1] + ((destination[1] - t.pos()[1] ) / 2)
    t.goto(x, y)

origins = []
t.speed(0)
t.penup()
height = math.sqrt(size**2 - (size/2)**2)
t.goto(-size/2, -height/2)
for i in range(3):
    origins.append(t.pos())
    DrawPoint(t.pos()[0], t.pos()[1], t.heading())
    t.forward(size)
    t.left(120)

t.setheading(0)
gotoMiddle(origins[1])
DrawPoint(t.pos()[0], t.pos()[1], 0)
try:
    for i in range(30000):
        gotoMiddle(origins[randint(0, 2)])
        DrawPoint(t.pos()[0], t.pos()[1], 0)
except Exception as e:
    print(e)

turtle.update()
print("Finished")
turtle.done()
