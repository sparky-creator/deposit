import art

print(logo)

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw(cards):
    picked_card = random.choice(cards)
    return picked_card

def black_jack(cards):
    if sum(cards) == 21:
        flag_black_jack = True
    else:
        flag_black_jack = False
    return flag_black_jack

def card_count(cards):
    if 11 in cards and sum(cards) > 21:
        cards = [ 1 if x == 11 else x for x in cards]
        sum_card = sum(cards)
    else:
        sum_card = sum(cards)
    return sum_card


def winning_logic(user_cards,comp_cards):

    print(f"computer has a black jack {black_jack(comp_cards)}")
    comp_has_bj = black_jack(comp_cards)
    print(f"player has a black jack {black_jack(user_cards)}")
    usr_has_bj = black_jack(user_cards)
    #black jack logic
    if comp_has_bj == True and usr_has_bj ==False:
        comp_win = True
        game_vale = 1
    elif comp_has_bj == False and usr_has_bj ==True:
        user_win = True
        game_value = 2
    elif comp_has_bj == True and usr_has_bj == True:
        game_draw = True
        game_value = 0
    else:
        game_stay = True
        game_value = 10
    return game_value



user_cards = []
comp_cards = []

init_game = True

if init_game == True:
    for i in range(0,2):
        print(i)
        card_f_usr = draw(cards)
        card_f_comp = draw(cards)
        user_cards.append(card_f_usr)
        comp_cards.append(card_f_comp)

    print(f"COMP first Card {comp_cards[0]}")
    game_value = winning_logic(user_cards,comp_cards)
    print(game_value)
    print(f"computer has a black jack {black_jack(comp_cards)}")
    print(f"player has a black jack {black_jack(user_cards)}")

    if game_value ==1:
        print("COMP WINS BJ")
    elif game_value ==2:
        print("USR WINS BJ")
    else:
        if card_count(user_cards) > 21:
            print("BUSTED")
        else:
            print(user_cards)
            print(card_count(user_cards))
            print(comp_cards)
            print(card_count(comp_cards))
            print("Draw One More cards?")
            one_more = input("YES or NO").lower()

if one_more == 'yes':
    card_f_usr = draw(cards)
    user_cards.append(card_f_usr)
    print(f"new set of urs {user_cards}")
    print(card_count((user_cards)))
    if card_count(user_cards) >21:
        print("Busted")



