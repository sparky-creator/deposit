#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# print(timmy)
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name",["Pikachu", "Squirtle", "Charmander"])
table.align = "l"
table.add_column("Type",["Electric", "Water", "Fire"])

print(table)



