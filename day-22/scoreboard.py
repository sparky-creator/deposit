from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")
        self.right_score = 0
        self.left_score = 0
        self.update_score()

    def update_score(self):
        self.penup()
        self.goto(-70,240)
        self.write(self.left_score,font=('Arial', 40, 'normal'))
        self.goto(70, 240)
        self.write(self.right_score, font=('Arial', 40, 'normal'))
