from turtle import Turtle

class PrintState(Turtle):

    def __init__(self):
        super().__init__()
        self.cord_x = 0
        self.cord_y = 0


    def write_state(self, state_name):

        cursor_pen = Turtle()
        cursor_pen.hideturtle()
        cursor_pen.penup()
        cursor_pen.goto((self.cord_x, self.cord_y))
        cursor_pen.write(f"{state_name}")


