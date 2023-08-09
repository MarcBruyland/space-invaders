from turtle import Screen
from lasers import Lasers
from defense import Defense
from invaders import Invaders
from scoreboard import Scoreboard


from constants import WIDTH, HEIGHT, SLEEPING, SHOT_MOVE
import time
from math import sqrt

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT, startx=350, starty=10)  # screen size 1920 x  760
screen.bgcolor("black")
screen.title("SpaceInvaders")
screen.bgpic("Images/space_invaders_background.gif")


# screen.tracer(0)

screen.addshape('Images/invader.gif')
screen.addshape('Images/alien.gif')
screen.addshape('Images/spaceship.gif')
screen.addshape('Images/explosion.gif')
screen.addshape('Images/laser.gif')

scoreboard = Scoreboard()
invaders = Invaders()
defense = Defense()
lasers = Lasers()
laser = lasers.get_laser()

def calc_distance(x1, y1, x2, y2):
    return int(sqrt((x1-x2)**2 + (y1-y2)**2))


def configure_onkeys(laser):
    screen.onkey(laser.go_left, "Left")
    screen.onkey(laser.go_right, "Right")
    screen.onkey(laser.double_mvt_step, "plus")
    screen.onkey(laser.half_mvt_step, "minus")
    screen.onkey(laser.shoot, " ")


screen.listen(xdummy=None, ydummy=None)
configure_onkeys(laser)


game_is_on = True

while game_is_on:
    time.sleep(SLEEPING)

    if laser.shot.shooting:
        laser.shot.move("up")
        defense.remove_defense(laser.shot, 'up')
        for invader in invaders.invaders:
            if invader.state == "alive":
                if calc_distance(laser.shot.xcor(), laser.shot.ycor(), invader.xcor(), invader.ycor()) < SHOT_MOVE:
                    invader.hit()
                    laser.shot.deactivate()
                    scoreboard.increase_score(invader.points)

    invaders.move()
    for invader in invaders.invaders:
        if invader.shot.shooting:
            invader.shot.move("down")
            defense.remove_defense(invader.shot, 'down')
            if calc_distance(invader.shot.xcor(), invader.shot.ycor(), laser.xcor(), laser.ycor()) < SHOT_MOVE:
                laser.shot.deactivate()  # avoid frozen laser shot
                lasers.kill_active_laser()
                laser = lasers.get_laser()
                if not laser:
                    game_is_on = False
                    scoreboard.msg_end_of_game("Game Over - You loose")
                    break
                else:
                    configure_onkeys(laser)
                invader.shot.deactivate()

    invader = invaders.get_random_invader()  # random invader could be None
    if invader:
        invader.shot.activate(invader.xcor(), invader.ycor())
    if len(invaders.get_indices_of_active_invaders()) == 0:
        scoreboard.msg_end_of_game("Game Over - You win")
    screen.update()


screen.exitonclick()
