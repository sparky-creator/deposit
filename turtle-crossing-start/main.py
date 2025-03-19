import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.level_update()
screen.listen()
screen.onkey(tim.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()

    # successful
    if tim.is_at_finish() == True:
        tim.go_to_start()
        car_manager.leve_up()
        scoreboard.level_increase()

screen.exitonclick()
