import turtle
from random import randint, random


timmy = turtle.Turtle()
turtle.colormode(255)
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

timmy.speed(10)

def draw_spirograph(size_of_gap):
    for i in range(int(360/ size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() +10)


draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
