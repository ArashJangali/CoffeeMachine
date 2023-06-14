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
    "money": 0,
}



def check(drink, paid_amount, chosen_drink):
    cost = drink["cost"]
    water = drink["ingredients"]["water"]
    coffee = drink["ingredients"]["coffee"]

    resource_water = resources["water"]
    resource_coffee = resources["coffee"]

    if chosen_drink == "espresso":
        milk = 0
        resource_milk = 0
    else:
        milk = drink["ingredients"]["milk"]
        resource_milk = resources["milk"]

    if paid_amount >= cost and resource_water >= water and resource_milk >= milk and resource_coffee >= coffee:
        change = round((paid_amount - cost), 2)
        resources["water"] -= water
        resources["coffee"] -= coffee
        if chosen_drink != "espresso":
            resources["milk"] -= milk
        make_coffee(chosen_drink, change)
    elif paid_amount < cost:
        print("Sorry that's not enough money. Money refunded.")
    elif resource_water < water:
        print("Not enough water")
    elif resource_milk < milk and drink != "espresso":
        print("Not enough milk")
    elif resource_coffee < coffee:
        print("Not enough coffee")
    else:
        print("Not enough resources")


def make_coffee(chosen_drink, change):

    print(f"Here is ${change} in change.")
    print(f"Here is your {chosen_drink} ☕️. Enjoy")
    machine()


def machine():

    chosen_drink = input("What would you like? (espresso/latte/cappuccino): ")

    if chosen_drink == "off":
        print("Turning off the machine.")
        return
    elif chosen_drink == "report":
        print("Water: ", resources["water"], "Milk: ", resources["milk"], "Coffee: ", resources["coffee"])
        machine()
    elif chosen_drink == "latte" or chosen_drink == "espresso" or chosen_drink == "cappuccino":
        drink = MENU[chosen_drink]
        print("Please insert coins.")
        quarters = (float(input("How many quarters?: ")) * 0.25)
        dimes = (float(input("how many dimes?: ")) * 0.1)
        nickels = (float(input("how many nickles?: ")) * 0.05)
        pennies = (float(input("how many pennies?: ")) * 0.01)
        paid_amount = quarters + dimes + nickels + pennies
        check(drink, paid_amount, chosen_drink)
    else:
        print("Invalid input. Come back later.")


machine()