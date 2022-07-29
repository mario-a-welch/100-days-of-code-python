from art import logo

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

is_on = True


def report():
    """Displays report of available resources and profit"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def is_enough_resources(necessary_resources):
    """Returns True when there are enough ingredients and False if resources are insufficient"""
    for item in necessary_resources:
        if necessary_resources[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def processed_coins():
    """Returns the total amount from the coins inserted"""
    print("Please insert coins for payment.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_processed_coins_enough(coins_processed, coffee_cost):
    """Returns True when processed_coins is greater than or equal to coffee cost or False if processed_coins is less
    than coffee cost"""
    if coins_processed >= coffee_cost:
        change = round(coins_processed - coffee_cost, 2)
        print(f"You paid too much! Here is ${change} in change.")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry, you did not enter enough money for the coffee. Money Refunded")
        return False


def make_coffee(coffee_name, necessary_resources):
    """Subtracts the necessary ingredients for the coffee from the resources"""
    for item in necessary_resources:
        resources[item] -= necessary_resources[item]
    print(f"Your order is ready! Enjoy your {coffee_name}!")


print(logo)

while is_on:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): \"Type 'off' to close\" - ")
    if customer_choice == "off":
        print("GoodBye!")
        is_on = False
    elif customer_choice == "report":
        report()
    else:
        drink = MENU[customer_choice]
        if is_enough_resources(drink["ingredients"]):
            payment = processed_coins()
            if is_processed_coins_enough(payment, drink["cost"]):
                make_coffee(customer_choice, drink["ingredients"])
