import random
from art import logo




def set_difficulty(dif):
	if dif == 'easy':
		counter = 10
	elif dif == 'hard':
		counter = 5
	return counter

def compare(guess):
	if guess == num:
		print(f"You got it! The answer was {guess}.")
		exit()
	elif guess > num:
		print(f"Too high.")
	elif guess < num:
		print(f"Too low.")
		
def play():
	print(logo)
	print("Welcome to the Number Guessing game!")
	print("I'm thinking of a number between 1 and 100.")
	
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
	attempts = set_difficulty(difficulty)

	num = random.randint(1,100)

	while attempts > 0:
		print(f"You have {attempts} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		compare(guess)
	
		attempts -= 1
		if attempts >0:
			print("Guess Again.")
		else:
			print("You've run out of guesses, you lose.")

play()



