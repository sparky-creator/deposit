from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def substract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1/n2

operations = {"+": add,
             "-": substract,
             "*": multiply,
             "/": divide,
             }
at_stop = False
init_result = 0
first_cal = True
while not at_stop:

    if first_cal:
        first_num = float(input("please enter your first number\n"))

    ask_operation = input("please enter your operation\n")
    second_num = float(input("please enter your second number\n"))

    if not first_cal:
        first_num = init_result

    result = operations[ask_operation](first_num, second_num)
    init_result = result
    print(init_result)

    ask_stop = input("do you want to continue").lower()
    if ask_stop == "no":
        at_stop = True
    else:
        first_cal = False

