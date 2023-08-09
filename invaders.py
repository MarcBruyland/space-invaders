from turtle import Turtle
from constants import WIDTH, INVADERS_ROWS, INVADERS_COLS
from shot import Shot
import random

class Invaders():
    def __init__(self):
        self.invaders = []
        for c in range(INVADERS_COLS):
            self.invaders.append(Invader(0, c,"Images/alien.gif"))
        for c in range(INVADERS_COLS):
            self.invaders.append(Invader(1, c,"Images/spaceship.gif"))
        for c in range(INVADERS_COLS):
            self.invaders.append(Invader(2, c,"Images/invader.gif"))
        self.direction = "right"

    def move(self):
        if self.invaders[INVADERS_COLS - 1].xcor() > 278:
            self.direction = "left"
        if self.invaders[0].xcor() < -278:
            self.direction = "right"

        for invader in self.invaders:
            if self.direction == "left":
                invader.move_left()
            elif self.direction == "right":
                invader.move_right()

    def get_indices_of_active_invaders(self):
        result = []
        ix = 0
        for invader in self.invaders:
            if invader.state == "alive":
                result.append(ix)
            ix += 1
        return result

    def get_random_invader(self):
        lst = self.get_indices_of_active_invaders()
        if lst:
            choice = random.choice(lst)
            if (choice + INVADERS_COLS in lst) or (choice + 2 * INVADERS_COLS in lst):
                return None
            else:
                return self.invaders[choice]
        else:
            return None


class Invader(Turtle):
    def __init__(self, row, col, filename):
        super().__init__()
        self.state = "alive"
        self.hideturtle()
        self.shape(filename)
        self.penup()
        x = -250 + int(col * WIDTH / 20)
        y = 250 - row * 35
        self.goto(x, y)
        self.showturtle()
        self.shot = Shot("invader")
        self.points = 30 - row * 10
    def move_left(self):
        self.goto(self.xcor() - 10, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 10, self.ycor())

    def hit(self):
        self.shape("Images/explosion.gif")
        self.hideturtle()
        self.state = "dead"

    def shoot(self):
        if not self.shot.shooting:
            self.shot.activate(self.xcor(), self.ycor())




