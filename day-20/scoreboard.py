from turtle import Turtle
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()


        # board = Turtle()
        # board.pen()
        # board.write("Score:", True, align="center")

    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score} High Score: {self.high_score}", align=ALIGNMENT, font=("Arial", 20, "normal") )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()