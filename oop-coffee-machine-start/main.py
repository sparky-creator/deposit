from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_machine_menu = Menu()
new_maker = CoffeeMaker()
new_trans = MoneyMachine()

stop_machine = False

while not stop_machine:

    print(new_maker.report())
    usr_input = input(f"what do you like {new_machine_menu.get_items()}\n")

    # usr_drink is Object with cost and ingredients attributes from MenuItem Class
    usr_drink = new_machine_menu.find_drink(usr_input)

    #check if we have enough resource

    if new_maker.is_resource_sufficient(usr_drink) == True:
        print(f"the cost of {usr_drink.name} is {usr_drink.cost}")
    # print("enter your money\n")
        value_payment = new_trans.make_payment(usr_drink.cost)
    if value_payment == True:
        print(f"here is your {usr_drink.name}")
        new_maker.make_coffee(usr_drink)
        print(new_trans.report())
        print(new_maker.report())
    else:
        print(f"SORRY, not enough resource")
        stop_machine = True