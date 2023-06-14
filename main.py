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

machine_on = True

def check(drink, paid_amount):
    cost = drink["cost"]
    water = drink["ingredients"]["water"]
    milk = drink["ingredients"]["milk"]
    coffee = drink["ingredients"]["coffee"]

    resource_water = resources["water"]
    resource_milk = resources["milk"]
    resource_coffee = resources["coffee"]

    if paid_amount >= cost and resource_water >= water and resource_milk >= milk and resource_coffee >= coffee:
        make_coffee()
    else:
        print("not enough resources")


def make_coffee():
    print("making coffee")

def machine():

    answer = input("What would you like? (espresso/latte/cappuccino): ")

    if answer == "report":
        print("Water: ", resources["water"], "Milk: ", resources["milk"], "Coffee: ", resources["coffee"])
    elif answer == "latte" or answer == "espresso" or answer == "cappuccino":
        drink = MENU[answer]
        print("Please insert coins.")
        quarters = (float(input("How many quarters?: ")) * 0.25)
        dimes = (float(input("how many dimes?: ")) * 0.1)
        nickels = (float(input("how many nickles?: ")) * 0.05)
        pennies = (float(input("how many pennies?: ")) * 0.01)
        paid_amount = quarters + dimes + nickels + pennies
        check(drink, paid_amount)
    else:
        print("Invalid input. Come back later.")

machine()

