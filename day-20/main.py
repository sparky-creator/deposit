from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
from types import new_class

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = ScoreBoard()
# starting_positions = [(0,0),(-20,0),(-40,0)]
#
# segments = []
# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

snake = Snake()

food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()

    #colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.rest()

    for segment in snake.segments[1:]:
        if  snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.rest()

    # for seg_num in range(2, 0, -1):
    #     new_x = segments[seg_num -1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)


screen.exitonclick()

