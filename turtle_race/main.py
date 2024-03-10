import turtle as turtle_module
import random

screen = turtle_module.Screen()
screen.setup(width=500, height=400)
colors = ['blue', 'red', 'green', 'yellow', 'orange', 'purple']
bet = False
while bet == False:

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet in colors:
        print(user_bet)
        bet = True
    else:
        print(f"Please choose one of the colors: {colors}")


turts = []


def check_turtle_finish(list_of_turtles):
    for turt in range(len(list_of_turtles)):
        if list_of_turtles[turt].position()[0] <= 250:
            continue
        else:
            return False
    return True

def check_for_winner(list_of_turtles):

    winner = None
    winner_pos =250
    for turt in range(len(list_of_turtles)):
        if (winner is None) or (list_of_turtles[turt].position()[0] > winner_pos):
            winner = list_of_turtles[turt].color()[0]
    print(f"The winner is {winner}!")





start_posx = -250
start_posy = -100

for i in range(6):
    turts.append(turtle_module.Turtle(shape='classic'))
    turts[i].color(colors[i])

    # turts[i].penup()
    turts[i].goto(start_posx, start_posy)
    start_posy += 50

while check_turtle_finish(turts):

    for i in range(6):
        turts[i].forward(random.randint(1, 10))

winner = check_for_winner(turts)

if winner == user_bet:
    print("You turtle won.")
else:
    print("Your turtle lost.")


screen.exitonclick()
