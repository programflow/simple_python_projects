from art import logo
import random
import time


## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1
## Use the folloowing list as the deck of cars:



## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn



def deal(hand):
	card_1 = cards[random.randint(0,len(cards)-1)]
	hand.append(card_1)
	cards.remove(card_1)
	card_2 = cards[random.randint(0,len(cards)-1)]
	hand.append(card_2)
	cards.remove(card_2)

	
def draw(hand):
	card = cards[random.randint(0,len(cards)-1)]
	hand.append(card)
	cards.remove(card)

def sum_hand(hand):
	if sum(hand) == 21 and len(hand) == 2:
		return 0
	if 11 in hand and sum(hand) > 21:
		hand.remove(11)
		hand.append(1)
	return sum(hand)


def compare(user_score, computer_score):


	if user_score > 21 and computer_score > 21:
		return "You went over. You lose 😤"


	if user_score == computer_score:
		return "Draw 🙃"
	elif computer_score == 0:
		return "Lose, opponent has Blackjack 😱"
	elif user_score == 0:
		return "Win with a Blackjack 😎"
	elif user_score > 21:
		return "You went over. You lose 😭"
	elif computer_score > 21:
		return "Opponent went over. You win 😁"
	elif user_score > computer_score:
		return "You win 😃"
	else:
		return "You lose 😤"


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == 'y':
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4



	print(logo)

	# we create empty hands and deal cards
	player_hand = []
	dealer_hand = []
	

	deal(player_hand)
	deal(dealer_hand)

	print(f"	Your cards: {player_hand}, curent score: {sum_hand(player_hand)}")
	print(f"	Computer's first card: {dealer_hand[0]}")

	hit = input("Type 'y' to get another card, type 'n' to pass: ")
	
	while hit == 'y':
		
		
		draw(player_hand)
		print(f"	Your cards: {player_hand}, curent score: {sum_hand(player_hand)}")
		if sum_hand(dealer_hand) < 17:
			draw(dealer_hand)
		print(f"	Computer's first card: {dealer_hand[0]}")

		if (sum_hand(player_hand) > 21) or (sum_hand(dealer_hand) > 21):
			hit = 'n'
		else:
			hit = input("Type 'y' to get another card, type 'n' to pass: ")

	print(f"	Your final hand: {player_hand}, final score: {sum_hand(player_hand)}")

	print(f"	Computer's final hand: {dealer_hand}, final score; {sum_hand(dealer_hand)}")

	print(compare( sum_hand(player_hand), sum_hand(dealer_hand)))


	play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")










