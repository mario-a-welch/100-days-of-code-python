from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Print report and take payment
money_machine = MoneyMachine()

# Print report of all resources, check to see if resources are sufficient, and make coffee
coffee_maker = CoffeeMaker()

# Returns names of available menu items, and searches menu for particular drink
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    customer_choice = input(f"What would you like to drink? ({options}) - ").lower()
    if customer_choice == "off":
        print("GoodBye!")
        is_on = False
    elif customer_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(customer_choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
