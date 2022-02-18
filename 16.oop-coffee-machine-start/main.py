from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_m = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    coffee = input(f"Choose your coffee ({options}): ")
    if coffee == "off":
        is_on = False
    elif coffee == "report":
        coffee_maker.report()
        money_m.report()
    else:
        choice = menu.find_drink(coffee)
        if coffee_maker.is_resource_sufficient(choice) and money_m.make_payment(choice.cost) == True:
           coffee_maker.make_coffee(choice)
    