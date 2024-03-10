import turtle
from random import randint, random


timmy = turtle.Turtle()
turtle.colormode(255)
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)
timmy.pensize(15)
timmy.speed(8)

for i in range(200):
    timmy.setheading(90*randint(0,4))
    timmy.pencolor(random_color())
    timmy.forward(30)

screen = Screen()
screen.exitonclick()
