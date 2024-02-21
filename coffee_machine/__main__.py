# coffe machine

# 1. Makes 3 hot flavors
# - espresso   - 50ml water,  18g Coffee               - $1.50
# - latte      - 200ml water, 24g Coffee, 150ml Milk   - $2.50
# - cappuccino - 250ml water, 24g Coffee, 100ml Milk   - $3.00
# Coffee Machine resources -
# - 300ml water, 200ml milk, 100g Coffee

# 2. Coin Operated (4 coins)
# - penny, nickel, dime, quarter

# Program Requirements

# Dictionary of drink choices and respective ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# list of resources left
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(money):
    """ Prints the resources and money taken"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink_ingredients):
    """ Checks to make sure there are enough resources to make requested drink."""
    for ingredient in drink_ingredients:
        if resources[ingredient] > drink_ingredients[ingredient]:
            continue
        else:
            return False
    return True


def process_payment(drink_price, money):
    """ Processes payment and returns change."""
    print("Please insert coins.")
    payment = 0
    quarters = int(input("How many quarters? "))
    payment += quarters * .25
    dimes = int(input("How many dimes? "))
    payment += dimes * .10
    nickels = int(input("How many nickels? "))
    payment += nickels * .05
    pennies = int(input("How many pennies? "))
    payment += pennies * .01
    if payment >= drink_price:
        change = payment - drink_price
        money += drink_price
        print(money)
        print(f"Here is ${change} in change.")
        return True, money
    else:
        return False, money


def make_coffee(drink_ingredients):
    """ Deducts resources used to make drink. """
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]


def start_coffee_machine():
    """ Runs coffee machine."""
    running = True
    money = 0
    while running:

        command = input('What would you like? (espresso/latte/cappuccino): ')

        if command.lower() == "report":
            report(money)

        elif command in MENU:
            enough_resources = check_resources(MENU[command]['ingredients'])

            if enough_resources:
                payment_successful, money = process_payment(MENU[command]['cost'], money)

                if payment_successful:
                    make_coffee(MENU[command]['ingredients'])
                    print(f"Here is your {command} ☕ Enjoy!")
                else:
                    print("Sorry that's not enough Money. Money refunded.")

            else:
                print("Not enough resources.")
        elif command == 'off':
            running = False


start_coffee_machine()
