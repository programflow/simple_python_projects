from color import generate_colors
import turtle
from random import choice


turtle.colormode(255)

timmy = turtle.Turtle()
timmy.speed(10)
timmy.shape("circle")

timmy.penup()
timmy.setx(-300)
timmy.sety(300)

for y in range(10):
    timmy.right(90)
    timmy.forward(50)
    timmy.left(90)
    for i in range(10):
        # timmy.color(choice(generate_colors()))
        timmy.forward(50)
        timmy.dot(20,choice(generate_colors()))
    timmy.backward(500)

timmy.ht()
screen = turtle.Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
screen.exitonclick()
