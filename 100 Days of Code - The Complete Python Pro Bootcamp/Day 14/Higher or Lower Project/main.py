from game_data import data
from art import logo
import random


# fetching random data to compose question

def fetch_data(choice):
    chosen_person = random.choice(data)
    # print(chosen_person)
    chosen_index = data.index(chosen_person)
    print(f"index {chosen_index}\n")
    print(f"comparison {choice}: {chosen_person['name']}, {chosen_person['description']}, from {chosen_person['country']}")
    count = chosen_person["follower_count"]
    return chosen_index, count

score = 0
game_over = False
first_rnd = True
# posing the question
while not game_over:
    print(logo)
    if first_rnd ==True:
        first_index, first_count  = fetch_data("A")
        print(first_count)
        second_index, second_count = fetch_data("B")
        print(second_count)
    else:
        print(f"your current score is {score}")
        first_update = data[first_index]
        print(f"comparison A: {first_update['name']}, {first_update['description']}, from {first_update['country']}")
        print(first_count)
        second_index, second_count = fetch_data("B")
        print(second_count)

    usr_answer = input("your guess?\n").lower()
    print(usr_answer)
    if usr_answer == "a":
        usr_count = first_count
        usr_index = first_index
        comp_count = second_count
    else:
        usr_count = second_count
        usr_index = second_index
        comp_count = first_count

    if usr_count < comp_count:
        print("GAME OVER")
        game_over = True
    else:
        score +=1
        print(score)
        first_rnd = False
        #update first question
        first_index = usr_index
        first_count = usr_count



#Compare A: Jennifer Lopez, a Musician and actress, from United States