from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_coffee_maker = CoffeeMaker()
new_menu = Menu()
new_money_mahcine = MoneyMachine()
machine = True
while machine:
    x = input("What would you like? ")
    # Prints report
    if x == "report":
        new_coffee_maker.report()
        new_money_mahcine.report()
    elif x == "menu":
        print(new_menu.get_items())

    elif x in new_menu.get_items():
        order = new_menu.find_drink(x)

        #checks if there are enough resources
        if new_coffee_maker.is_resource_sufficient(order):
            # processes coins and checks transaction
            if new_money_mahcine.make_payment(order.cost):
                new_coffee_maker.make_coffee(order)
    elif x == "off":
        machine = False




