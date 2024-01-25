
# this library will used to pick a random word from hangman_words.py
import random

from hangman_words import word_list

number = random.randint(0, len(word_list))
word = list(word_list[number])
reference_word = word.copy()


from hangman_art import logo, stages

print(logo)




letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



def create_answer(w):
	answer = []
	for i in range(len(w)):
		answer.append("_")
	return answer



def check_valid_guess(l):
	if l in letters:
		return True
	else:
		return False

def check_guessed_letters(l):
	if l not in guessed_letters:
		return True
	else:
		return False

def check_word(l):
	if l in word:
		return True
	else:
		return False

guessed_letters = []

def print_info():
	print("The letter you've guessed are:")
	print(guessed_letters)

guess_word = create_answer(word)
print(guess_word)







death_counter =7
while guess_word.count("_") != 0:
	guess = input("Guess a letter: ")
	if len(guess) == 1:
		if check_valid_guess(guess):
			if check_guessed_letters(guess):
				guessed_letters.append(guess)
				if check_word(guess):
					while guess in word:
						guess_word[word.index(guess)] = guess
						word[word.index(guess)] = "_"
					print("You got a guess right!")
					print_info()
				else:
					print("That letter is not in the word. Guess again.")
					print_info()
					death_counter -= 1
					print(stages[death_counter])

					if death_counter == 0:
						print("You're dead. Better luck next time bitch!")
						print("The word was "+ "".join(reference_word))
						exit()

					continue
			else:
				print("You already guessed that letter.")
				print_info()

				continue
		else:
			print("Please guess a letter")
			print_info()

			continue
		print(guess_word)

	elif len(guess) > 1:
		x = input("Are you sure you want to guess the word? It's all or nothing?(yes/no)")
		if x.lower() == "yes":	
			if guess == "".join(reference_word):
				print("You guessed the word!!!")
				break
			else:
				print("You're dead. Better luck next time bitch!")
				print("The word was "+ "".join(reference_word))
				exit()

			

print("Noice!! You escaped death you lucky bitch!!")

		

# Assume that all the letters of the word are non repeating
# Assume that every guess is a correct guess
# Problem 1: we need a way of checking repeating guesses so that it's removed from the pool 
# of valid guesses
# 

