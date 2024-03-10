import turtle as turtle_module
from turtle import _Screen

timmy = turtle_module.Turtle()
screen = turtle_module.Screen()

def forward_button():
    timmy.forward(10)
def backward_button():
    timmy.backward(10)
def right_turn():
    timmy.right(10)
def left_turn():
    timmy.left(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.onkey(fun=forward_button, key="w" )
screen.onkey(fun=backward_button, key="s")
screen.onkey(fun=right_turn, key="d")
screen.onkey(fun=left_turn, key="a")
screen.onkey(fun=clear, key="c")

screen.listen()


screen.exitonclick()