from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
#tim.color("red")

# for _ in range(4):
#     tim.fd(100)
#     tim.pendown()
#     tim.lt(90)
#     #tim.penup()

# def dashed_line(distance):
#     for _ in range(distance):
#         fraction =2
#         for i in range(fraction):
#             tim.pendown()
#             tim.fd(distance/fraction)
#             tim.penup()
#             tim.fd(distance / fraction)
#
# dashed_line(10)


# draw_diction={
#     "triangle": {"side":3,"color":"black"},
#     "square": {"side":4,"color":"red"},
#     "pentagon": {"side":5,"color":"blue"},
#     "hexagon": {"side":6, "color": "purple"},
#     "heptagon": {"side":7,"color":"red"},
#     "octagon": {"side":8,"color":"blue"},
#     "nanoagon": {"side":9, "color": "purple"},
#     "decagon": {"side": 10, "color": "purple"},
#               }
# num_side = draw_diction["triangle"]["side"]
#
# #print(angle)
# for key in draw_diction:
#     num_side = draw_diction[key]["side"]
#     draw_color = draw_diction[key]["color"]
#     for _ in range(num_side):
#         tim.color(draw_color)
#         tim.fd(100)
#         tim.lt(360/num_side)

list_of_actions = ["forward", tim.backward(5), tim.left(90), tim.right(90)]
import random

for _ in range(100):
    random.choice(list_of_actions)

screen = Screen()
screen.exitonclick()
