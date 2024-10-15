from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

is_off = False
while not is_off:
    choice = input(f"What would you like? ({menu.get_items()}): \n")
    if choice == "off":
        is_off = True
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink):
           if my_money_machine.make_payment(drink.cost):
               my_coffee_maker.make_coffee(drink)
