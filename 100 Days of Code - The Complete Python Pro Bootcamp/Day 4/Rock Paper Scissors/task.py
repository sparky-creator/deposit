rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

poss_choices = ["rock", "paper", "scissors"]
poss_graphics = [rock, paper, scissors]

usr_input = input("type your choice? ")

computer_choice = poss_choices[random.randint(0,2)]

print(usr_input)

if usr_input == computer_choice:
    print("try again, TIE")
else:
    if usr_input == "rock":
        if computer_choice == "paper":
            print("you lost")
        else:
            print("you won")
    elif usr_input =="paper":
        if computer_choice == "rock":
            print("you won")
        else:
            print("you lost")
    elif usr_input =="scissors":
        if computer_choice == "rock":
            print("you lost")
        else:
            print("you won")


