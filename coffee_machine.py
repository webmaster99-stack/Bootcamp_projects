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

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, we dont have enough {item} ")
            return False
        else:
            return True


def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received: float, order_price: float):
    if money_received >= order_price:
        change = round(money_received - order_price)
        print(f"Here is ${change} of change")
        global profit
        profit += order_price
        return True
    else:
        print("Sorry, you dont have enough money. Money refunded")
        return False


def make_coffee(drink_name: str, order_ingredients: str):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


profit = 0
is_off = False

while not is_off :
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_off = True
    elif choice == "report":
        print(f"Water: {resources["water"]}\n"
              f"Milk: {resources["milk"]}\n"
              f"Coffee:{resources["coffee"]}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
