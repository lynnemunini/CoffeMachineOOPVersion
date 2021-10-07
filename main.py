from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_money_machine = MoneyMachine()
my_money_machine.report()
my_coffee_maker = CoffeeMaker()
my_coffee_maker.report()
menu = Menu()
while True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "off":
        break
    elif choice == "report":
        my_money_machine.report()
        my_coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)



