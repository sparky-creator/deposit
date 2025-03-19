from turtle import Turtle, Screen
import random
import time
screen = Screen()

screen.listen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle?")

abba = Turtle(shape="turtle")
abba.color("red")
abba.penup()
abba.goto(x=-230, y=-50)

omma = Turtle(shape="turtle")
omma.color("purple")
omma.penup()
omma.goto(x=-230, y=-100)

hanna = Turtle(shape="turtle")
hanna.color("blue")
hanna.penup()
hanna.goto(x=-230, y=10)


euna = Turtle(shape="turtle")
euna.color("black")
euna.penup()
euna.goto(x=-230, y=50)

all_turtles = [abba, omma, hanna, euna]
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle?")

if user_bet:
    is_race_on = True

while is_race_on:

    # rand_distance = random.randint(0,10)
    # abba.forward(rand_distance)
    # rand_distance = random.randint(0,10)
    # omma.forward(rand_distance)
    # rand_distance = random.randint(0,10)
    # hanna.forward(rand_distance)
    # rand_distance = random.randint(0,10)
    # euna.forward(rand_distance)

    for i in all_turtles:
        if i.xcor() > 230:
            wining_clor = i.pencolor()
            if wining_clor == user_bet:
                print(f"WINNER IS {wining_clor}, won")
                is_race_on = False
            else:
                print(f"WINNER IS {wining_clor}, lost")
                is_race_on = False
        else:
            time.sleep(0.1)
            if random.choice([1,2,4,5,6])==1:
                rand_distance = random.randint(0,10)*5
            else:
                rand_distance = random.randint(0, 10) * 1
            i.forward(rand_distance)



# # move_dic ={"W": tim.forward(),
# #            "S": tim.backward(10),
# #            "D": tim.right(5)
# #            "A": tim.left(5)
# #            "C": clearscreen()
# #
# #            }
#
#
#
# def move_for():
#     tim.forward(10)
#
# def move_back():
#     tim.backward(10)
#
# def clock_wise():
#     tim.right(5)
#
# def anti_clock():
#     tim.left(5)
#
#
# screen.onkey(key="w", fun=move_for)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=clock_wise)
# screen.onkey(key="d", fun=anti_clock)
# screen.onkey(key="c", fun=screen.clearscreen)

screen.exitonclick()