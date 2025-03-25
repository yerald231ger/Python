from random import choice

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from another_module import CustomPrettyTable

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_table = CustomPrettyTable()
my_menu = Menu()

# Print the Menu with prices in the CustomPrettyTable
my_table.field_names = ["Drink", "Cost"]
for item in my_menu.menu:
    my_table.add_row([item.name, item.cost])

print(my_table)

is_on = True

while is_on:
    options = my_menu.get_items() + "off|report"
    choice = input(f"What would you like? {options}: ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        my_money_machine.report()
        my_coffee_maker.report()
    else:
        drink = my_menu.find_drink(choice)
        if drink is not None:
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)
                    my_table.field_names = ["Drink", "Cost"]
                    my_table.add_row([drink.name, drink.cost])
                    print(my_table)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough resources.")
        else:
            print("Sorry that item is not available.")