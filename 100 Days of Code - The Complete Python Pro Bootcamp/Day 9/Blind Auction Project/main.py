# TODO-1: Ask the user for input
# name = input("please enter your name to bid\n")
# price = input("please enter amount of bid\n")
# stop_bid = input("please enter Yes to continue or No to stop").lower()
from art import logo

print(logo)
bid_continue = True
book = {}

while bid_continue:
    name = input("please enter your name to bid\n")
    price = input("please enter amount of bid\n")
    check = price.replace("$","")
    bid_amount = int(check.replace("$",""))

    book[name] =bid_amount

# TODO-2: Save data into dictionary {name: price}

    play_bid = input("please enter y to continue or No to stop").lower()
    if play_bid == "y":
        bid_continue = False
    # else:
    #     bid_continue = True

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
Max_bidder = ""
max = 0
for key in book:
    if book[key] > max:
        Max_bidder = key
        max = book[key]
print(book)
print(f"winner {Max_bidder} bid {book[Max_bidder]}")