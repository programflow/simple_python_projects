from turtle import Turtle, Screen
from random import random

timmy = Turtle()

angle = 0
sides = 2


for n in range(10):
    timmy.pencolor((random(), random(), random()))
    angle += 180
    sides += 1
    for i in range(sides):

        timmy.forward(100)
        timmy.right(180 - angle / sides)


screen = Screen()
screen.exitonclick()
