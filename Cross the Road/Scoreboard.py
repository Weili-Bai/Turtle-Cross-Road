from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self, window):
        super().__init__()
        self.game_speed = 0.1
        self.level = 1
        self.penup()
        x = 40 - window.window_width() / 2
        y = window.window_height() / 2 - 40
        self.goto(x, y)
        self.hideturtle()
        self.write_board()

    def write_board(self):
        self.clear()
        self.write(f"Level:{self.level}", align=ALIGN, font=FONT)
