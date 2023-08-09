from turtle import Turtle
from constants import WIDTH, HEIGHT

FONT = ("Courier", 15, "normal")

print(WIDTH, HEIGHT)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        x = WIDTH / 2 - 75
        y = -HEIGHT / 2 + 40
        self.goto(x, y)
        self.write(f"{self.score} points", align="right", font=FONT)

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def msg_end_of_game(self, msg):
        x = -WIDTH / 8 - 30
        print(FONT[1], x, len(msg))
        y = -HEIGHT / 2 + 40
        self.goto(x, y)
        self.write(msg, align="left", font=FONT)
