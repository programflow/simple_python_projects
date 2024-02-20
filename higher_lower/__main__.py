import random
from game_data import data
import art


score = 0
continue_game = True
while continue_game == True:
	item_A = data[random.randint(0, len(data)-1)]
	item_B = data[random.randint(0, len(data)-1)]
	print(art.logo)
	print(f"Compare A: {item_A['name']}, a {item_A['description']}, from {item_A['country']}")
	print(art.vs)
	print(f"Against B: {item_B['name']}, a {item_B['description']}, from {item_B['country']}")
	choice = input("Who has more followers? Type 'A' or 'B': ")

	if item_A['follower_count'] > item_B['follower_count']:
		correct_answer = "A"
	else:
		correct_answer = "B"

	if choice == correct_answer:
		score += 1
		print(f"You're right! Current score: {score}")
	else:
		print(f"Sorry, That's wrong. Final score: {score}")
		continue_game = False


