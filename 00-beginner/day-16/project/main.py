from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Get the list of items from the Menu class
menu = Menu()
# Create the coffee maker object
coffee_maker = CoffeeMaker()
# Create the money machine object
money_machine = MoneyMachine()

is_on = True

while is_on:
    # Print the greeting message
    choice = input(f"What would you like? ({menu.get_items()}): ")

    # Check inputs given by the user
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(choice) != None:
        # Get the drink from the menu
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

