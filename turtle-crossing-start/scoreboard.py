from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-200,260)
        self.level_update()


    def level_update(self):
        self.clear()
        self.write(f"LEVEL:{self.level}",align="left", font=FONT)

    def level_increase(self):
        self.level += 1
        self.level_update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",font=FONT)