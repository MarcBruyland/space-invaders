from turtle import Turtle
from constants import HEIGHT, SHOT_MOVE, INVADER_HEIGHT


class Shot(Turtle):
    def __init__(self, shot_type):
        super().__init__()
        self.hideturtle()
        self.shooting = False
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.shot_type = shot_type
        if shot_type == "laser":
            self.left(90)
        elif shot_type == "invader":
            self.right(90)

    def activate(self, x, y):
        print(f"Shot.activate shooting = {self.shooting}")
        if not self.shooting:
            self.shooting = True
            self.penup()
            self.goto(x, y)
            self.showturtle()

    def deactivate(self):
        self.hideturtle()
        self.shooting = False
        self.penup()
        self.goto(0,0)

    def move(self, direction):
        if direction == "up":  # laser
            self.goto(self.xcor(), self.ycor() + SHOT_MOVE)
        elif direction == "down":  # invader
            self.goto(self.xcor(), self.ycor() - SHOT_MOVE)
        if self.ycor() > HEIGHT / 2 or self.ycor() < - HEIGHT / 2:
            self.deactivate()