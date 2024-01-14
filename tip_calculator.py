print("Welcome to the tip calculator.")
total_bill = input("What was the the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")


tip_dollars = float(tip_percent)*.01*float(total_bill)


bill_with_tip = float(total_bill) + tip_dollars

dollar_split = bill_with_tip / float(people)

print("Each person should pay: {}".format(round(dollar_split, 2)))
