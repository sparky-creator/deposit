MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" :  0,
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

# TODO: 1. print report


#usr_input = input("What would you like? (espresso/latte/cappuccino)\n").lower()


def transaction(total_usr_coin,ur_choice):
    if total_usr_coin <MENU[ur_choice]["cost"]:
        print("SORRY, NOT Enough FUND")
        action = "skip"
        flow ={}
    else:
        action = "dispense"
        print(f"you paid {total_usr_coin} and change {total_usr_coin- MENU[ur_choice]["cost"]}")
        flow = MENU[ur_choice]["ingredients"]

    return action, flow

def resource_balance(action, flow, resource):

    if action =="update_resource":
        for key in resource:
            resource[key] = resource[key] + flow[key]
        print(resource)
    elif action =="report":
        for key in resource:
            print(f" current resource {key} is {resource[key]}")
    elif action =="skip":
        print("Try again")
    else:  # dispensing the items
        for key in resource:
            print(resource)
            print(flow)
            resource[key] = resource[key] - flow[key]
        print(resource)

# action, flow = transaction(total_usr_coin, usr_choice)
#
# resource_balance(action, flow, resource)

# TODO : 2. ...
resource ={"water":1000, "milk": 1000, "coffee": 1000}

flow ={"water":100, "milk": 100, "coffee": 100}
# Turn off the coffee machine

off_machine = False

while not off_machine:
    usr_input = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    if usr_input == "off":
        off_machine = True
        print("Machine Off")
    elif usr_input == "report":
        # call report function
        usr_choice = usr_input
        resource_balance(usr_choice, {}, resource)
    else:
        usr_choice = usr_input
        # check remaing resource

        print(f"we chosen {usr_input} and cost {MENU[usr_input]["cost"]}")
        # tell users to insert money
        usr_quarter = int(input("HOW MANY Quarters\n"))
        usr_dime = int(input("HOW MANY Dimes\n"))
        usr_nickle = int(input("HOW MANY Nickles\n"))
        usr_penny = int(input("HOW MANY Pennies\n"))

        total_usr_coin = 0.25 * usr_quarter + 0.1 * usr_dime + 0.05 * usr_nickle + 0.01 * usr_penny

        action, flow = transaction(total_usr_coin,usr_choice)
        print(action)
        flow = MENU[usr_choice]["ingredients"]
        resource_balance(action,flow,resource)
    # refund, change and proceed function


        #make coffee, touch resource and enjo

