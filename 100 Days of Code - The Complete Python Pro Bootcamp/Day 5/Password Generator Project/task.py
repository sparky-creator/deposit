letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

total_letters, total_symbols, total_numbers, = "", "", ""

for choice in range(0,nr_letters):
    chosen_rand_letter = letters[random.randint(0,len(letters)-1)]
    print(type(chosen_rand_letter))
    total_letters = total_letters + chosen_rand_letter

print(total_letters)

for choice in range(0, nr_symbols):
    chosen_rand_sym = symbols[random.randint(0, len(symbols)-1)]
    total_symbols = total_symbols + chosen_rand_sym

print(total_symbols)

for choice in range(0, nr_numbers):
    chosen_rand_num = numbers[random.randint(0, len(numbers)-1)]
    total_numbers = total_numbers + chosen_rand_num

print(total_numbers)

total_password = total_numbers + total_symbols +total_letters
temp_letter = list(total_password)
print("first temp" + str(temp_letter))
random.shuffle(temp_letter)
print("shuffled temp" + str(temp_letter))
final_chosen_letter = ''.join(temp_letter)

print(final_chosen_letter)

