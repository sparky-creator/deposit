from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, cord = (350,0)):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.x_cord = cord[0]
        self.y_cord = cord[1]
        self.goto(self.x_cord, self.y_cord)

    def go_up(self):
        new_y = self.ycor()  + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


