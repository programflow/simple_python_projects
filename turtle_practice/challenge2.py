from turtle import Turtle, Screen



timmy = Turtle()
for i in range(8):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()



screen = Screen()
screen.exitonclick()