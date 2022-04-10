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


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')
    return True


def off():
    return False


def check_resources(drink):
    if drink["water"] > resources["water"]:
        print("Sorry there is not enough water")
        return False
    elif drink["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    elif "milk" in drink.keys():
        if drink["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
    return True


def cost(drink_cost):
    print("Please insert coins.")
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles?: ")) * 0.05
    pennies = float(input("how many dimes?: ")) * 0.01
    user_money = round((quarters + dimes + nickles + pennies), 2)
    if user_money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources["money"] += drink_cost
        change = round(user_money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True


def make_coffee(drink):
    resources["water"] -= drink["water"]
    if "milk" in drink.keys():
        resources["milk"] -= drink["milk"]
    resources["coffee"] -= drink["coffee"]


def espresso():
    drink = MENU["espresso"]["ingredients"]
    drink_cost = MENU["espresso"]["cost"]
    if check_resources(drink):
        if cost(drink_cost):
            make_coffee(drink)
            print("Here is your espresso ☕️. Enjoy!")
    return True


def latte():
    drink = MENU["latte"]["ingredients"]
    drink_cost = MENU["latte"]["cost"]
    if check_resources(drink):
        if cost(drink_cost):
            make_coffee(drink)
            print("Here is your latte ☕️. Enjoy!")
    return True


def cappuccino():
    drink = MENU["cappuccino"]["ingredients"]
    drink_cost = MENU["cappuccino"]["cost"]
    if check_resources(drink):
        if cost(drink_cost):
            make_coffee(drink)
            print("Here is your cappuccino ☕️. Enjoy!")
    return True


FUNCTION_DICT = {
    "report": report,
    "off": off,
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,
}

working = True
while working:
    working = FUNCTION_DICT[input("What would you like? (espresso/latte/cappuccino)")]()
