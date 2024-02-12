import os
clear = lambda: os.system("clear")
#do stuff

from art import logo

print(logo)


print("Welcome to the secret auction program.")
more_bidders = 'yes'
bid_log = {}
while more_bidders.lower() == "yes":
	name = input("What is your name? ")
	bid = input("What is your bid? $")
	bid_log[name] = bid
	more_bidders = input("Are there any other bidders? Type 'yes' or 'no. ")
	print("\r", end = "")
	clear()

highest_bid = 0
highest_bidder = None
for key in bid_log:
	if int(bid_log[key]) > highest_bid:
		highest_bid = int(bid_log[key])
		highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")