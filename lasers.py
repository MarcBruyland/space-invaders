from turtle import Turtle
from constants import WIDTH, HEIGHT, N_LIVES, MOVE_STEP, PADDING_LASER
from shot import Shot


class Lasers():
    def __init__(self):
        self.lasers = []
        for ix in range(N_LIVES):
            if ix == 0:
                x = 0
                y = -HEIGHT/2 + PADDING_LASER
            else:
                x = -WIDTH /2 + 75 + ix * 50
                y = -HEIGHT/2 + 40
            self.lasers.append(LaserShooter((x,y)))
        self.active = 0

    def get_laser(self):
        if self.active < N_LIVES:
            ix = self.active
            laser = self.lasers[ix]
            x = 0
            y = -HEIGHT / 2 + PADDING_LASER
            laser.penup()
            laser.goto(x, y)
            return laser
        else:
            return None

    def kill_active_laser(self):
        laser = self.get_laser()
        laser.hit()
        self.active += 1


class LaserShooter(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape('Images/laser.gif')
        self.penup()
        self.goto(position)
        self.showturtle()
        self.shot = Shot("laser")
        self.mvt_step = 4 * MOVE_STEP

    def go_left(self):
        new_x = self.xcor() - self.mvt_step
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + self.mvt_step
        self.goto(new_x, self.ycor())

    def double_mvt_step(self):
        self.mvt_step *= 2

    def half_mvt_step(self):
        if self.mvt_step > MOVE_STEP:
            self.mvt_step = int(self.mvt_step / 2)
        else:
            self.mvt_step = MOVE_STEP

    def shoot(self):
        print(f"LaserShooter.shoot: x {self.xcor()}, y {self.ycor()}")
        self.shot.activate(self.xcor(), self.ycor()+35)

    def hit(self):
        self.shape("Images/explosion.gif")
        self.hideturtle()
