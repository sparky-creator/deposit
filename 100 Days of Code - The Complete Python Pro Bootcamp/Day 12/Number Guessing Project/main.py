import random

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of 1 and 100\n")

level = input("choose easy or hard\n").lower()

if level == "easy":
    Total_trial = 10
else:
    Total_trial = 5



avail_trial = Total_trial
correct_guess = False

chosen_number = random.randint(1,101)
print(chosen_number)

def clue(guess_number):
    if chosen_number > guess_number:
        print("ur guess is too small\n")
    else:
        print("ur guess is too large\n")


def guess_correct(guess_number):
    flag_correct = False
    print(f"inner guess {guess_number}")
    print(f"chosen number {chosen_number}")
    if chosen_number == guess_number:
        flag_correct = True
    else:
        clue(guess_number)
    return flag_correct


while avail_trial > 0 and correct_guess == False:

    print(f"You have {avail_trial} to guess")
    guess_number = int(input("your guess\n"))
    result = guess_correct(guess_number)
    if result == True:
        correct_guess = True
    else:
        avail_trial -= 1
    print(result)



