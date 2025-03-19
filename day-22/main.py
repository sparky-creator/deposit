from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height= 600, width= 800)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle()
ball =Ball()

screen.listen()


screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

scoreboard = ScoreBoard()

game_is_on = True
dir_var = 1
while game_is_on:
    time.sleep(0.06)
    screen.update()

    ball.move()
# dectionn collision with wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        # needs bounce
        ball.bounce_y()
# detect collision with r_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# ball moves out of screen right_score
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.left_score +=1
        scoreboard.update_score()

        #ball.bounce_x()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.right_score += 1
        scoreboard.update_score()
        #ball.bounce_x()


screen.exitonclick()
