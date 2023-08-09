from turtle import Turtle
from constants import DEFENSE_START_X, DEFENSE_START_Y, DEFENSE_HEIGHT, DEFENSE_OG_GAP, \
                      DEFENSE_X_GAP, DEFENSE_REPEAT, DEFENSE_HEIGHT_SMALL, DEFENSE_DESTROY_PIXELS, \
                      DEFENSE_COLOR, DEFENSE_BG_COLOR


class Defense(Turtle):
    def __init__(self):
        super().__init__()
        self.lst_defense_elements = {}
        for x in range(DEFENSE_START_X, - DEFENSE_START_X):
            self.lst_defense_elements[x] = []
        self.hideturtle()
        self.speed(0)
        self.color(DEFENSE_COLOR)
        self.left(90)
        self.baseline_x = DEFENSE_START_X
        self.baseline_y = DEFENSE_START_Y
        self.offset_x = 0
        self.draw_G()
        self.draw_O()
        self.draw_O()
        self.draw_G()
        self.draw_L()
        self.draw_E()

    def add_defense(self, x, y_start, y_end):
        for y in range(y_start, y_end):
            self.lst_defense_elements[x].append(y)

    def remove_defense(self, shot, direction):
        x = shot.xcor()
        y = shot.ycor()
        if x in self.lst_defense_elements:
            length = len(self.lst_defense_elements[x])
            print()
            print(f"remove_defense: x: {x}, y: {y}, length: {length}, lst: {self.lst_defense_elements[x]}")
            if length > 0:
                if y >= self.lst_defense_elements[x][0] and direction == "up":
                    y_start = self.lst_defense_elements[x][0]
                    y_end = y_start + min(length, DEFENSE_DESTROY_PIXELS)
                    self.draw_it(x, y_start, y_end, DEFENSE_BG_COLOR)

                    if length > DEFENSE_DESTROY_PIXELS:
                        prev_y = self.lst_defense_elements[x][0]
                        for i in range(DEFENSE_DESTROY_PIXELS):
                            print(f"remove_defense - before pop: i: {i}, length: {len(self.lst_defense_elements[x])}, lst: {self.lst_defense_elements[x]}")
                            if self.lst_defense_elements[x][0] - prev_y <= 1:
                                prev_y = self.lst_defense_elements[x][0]
                                dummy = self.lst_defense_elements[x].pop(0)
                            else:
                                break
                            print(f"remove_defense - dummy: {dummy}")
                            print(f"remove_defense - after pop: i: {i}, length: {len(self.lst_defense_elements[x])}, lst: {self.lst_defense_elements[x]}")
                    else:
                        self.lst_defense_elements[x] = []
                        print(f"remove_defense - last: length: {len(self.lst_defense_elements[x])}, lst: {self.lst_defense_elements[x]}")

                    shot.deactivate()
                    print("remove_defense - shot reset")

                elif y <= self.lst_defense_elements[x][-1] and direction == "down":
                    y_start = self.lst_defense_elements[x][-1]
                    y_end = y_start - min(length, DEFENSE_DESTROY_PIXELS)
                    self.draw_it(x, y_start, y_end, DEFENSE_BG_COLOR)

                    if length > DEFENSE_DESTROY_PIXELS:
                        prev_y = self.lst_defense_elements[x][-1]
                        for i in range(DEFENSE_DESTROY_PIXELS):
                            print(f"remove_defense - before pop: i: {i}, length: {len(self.lst_defense_elements[x])}, lst: {self.lst_defense_elements[x]}")
                            if prev_y - self.lst_defense_elements[x][-1] <= 1:
                                prev_y = self.lst_defense_elements[x][-1]
                                dummy = self.lst_defense_elements[x].pop(-1)
                            else:
                                break
                            print(f"remove_defense - dummy: {dummy}")
                            print(f"remove_defense - after pop: i: {i}, length: {len(self.lst_defense_elements[x])}, lst: {self.lst_defense_elements[x]}")
                    else:
                        self.lst_defense_elements[x] = []
                        print(f"remove_defense - last: length: {len(self.lst_defense_elements[x])}, lst: {self.lst_defense_elements[x]}")

                    shot.deactivate()
                    print("remove_defense - shot reset")


    def draw_G(self):
        self.draw_line(3 * DEFENSE_OG_GAP, DEFENSE_HEIGHT - 6 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.draw_line(2 * DEFENSE_OG_GAP, DEFENSE_HEIGHT - 4 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.draw_line(DEFENSE_OG_GAP, DEFENSE_HEIGHT - 2 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.draw_line_interrupted(0, DEFENSE_HEIGHT, DEFENSE_REPEAT)
        self.draw_line_interrupted(0, DEFENSE_HEIGHT, DEFENSE_REPEAT)
        self.draw_lines_interrupted(0, DEFENSE_HEIGHT, DEFENSE_HEIGHT_SMALL, DEFENSE_REPEAT - 1)
        self.draw_lines_interrupted(0, DEFENSE_HEIGHT, 2*DEFENSE_HEIGHT_SMALL, DEFENSE_REPEAT - 1)
        self.draw_lines_interrupted(0, DEFENSE_HEIGHT, 3*DEFENSE_HEIGHT_SMALL, DEFENSE_REPEAT - 1)
        self.draw_line_interrupted2(0, DEFENSE_HEIGHT, 3*DEFENSE_HEIGHT_SMALL, DEFENSE_REPEAT-1)
        self.draw_line_interrupted2(DEFENSE_OG_GAP, DEFENSE_HEIGHT - 2 * DEFENSE_OG_GAP, 3*DEFENSE_HEIGHT_SMALL, DEFENSE_REPEAT-1)
        self.draw_line_interrupted2(2 * DEFENSE_OG_GAP, DEFENSE_HEIGHT - 4 * DEFENSE_OG_GAP, 2*DEFENSE_HEIGHT_SMALL, DEFENSE_REPEAT-1)
        self.draw_line_interrupted2(3 * DEFENSE_OG_GAP, DEFENSE_HEIGHT - 6 * DEFENSE_OG_GAP, DEFENSE_HEIGHT_SMALL, DEFENSE_REPEAT-1)
        self.offset_x += 3 * DEFENSE_X_GAP

    def draw_O(self):
        self.draw_line(3 * DEFENSE_OG_GAP, DEFENSE_HEIGHT - 6 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.draw_line(2 * DEFENSE_OG_GAP, DEFENSE_HEIGHT - 4 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.draw_line(DEFENSE_OG_GAP, DEFENSE_HEIGHT - 2 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.draw_line_interrupted(0, DEFENSE_HEIGHT, DEFENSE_REPEAT)
        self.draw_line_interrupted(0, DEFENSE_HEIGHT, DEFENSE_REPEAT)
        self.draw_line(DEFENSE_OG_GAP, DEFENSE_HEIGHT - 2 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.draw_line(2 * DEFENSE_OG_GAP, DEFENSE_HEIGHT - 4 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.draw_line(3 * DEFENSE_OG_GAP, DEFENSE_HEIGHT - 6 * DEFENSE_OG_GAP, DEFENSE_REPEAT)
        self.offset_x += 3 * DEFENSE_X_GAP

    def draw_L(self):
        self.draw_line(0, DEFENSE_HEIGHT, 3*DEFENSE_REPEAT)
        self.draw_line(0, int(DEFENSE_HEIGHT/5), 5*DEFENSE_REPEAT)
        self.offset_x += 3 * DEFENSE_X_GAP
    def draw_E(self):
        self.draw_line(0, DEFENSE_HEIGHT, 2*DEFENSE_REPEAT)
        self.draw_lines_interrupted(0, DEFENSE_HEIGHT, 4*DEFENSE_HEIGHT_SMALL, 5*DEFENSE_REPEAT)
        #print(self.lst_defense_elements)

    def draw_it(self, x, y_start, y_end, color):
        self.color(color)
        self.penup()
        self.goto(x, y_start)
        self.pendown()
        self.goto(x, y_end)
        if color == DEFENSE_COLOR:
            self.add_defense(x, y_start, y_end)

    def draw_line(self, offset_y, line_height, repeat):
        for i in range(repeat):
            x = self.baseline_x + self.offset_x
            y_start = self.baseline_y + offset_y
            y_end = self.baseline_y + offset_y + line_height
            self.draw_it(x, y_start, y_end, DEFENSE_COLOR)
            self.offset_x += DEFENSE_X_GAP

    def draw_line_interrupted(self, offset_y, line_height, repeat):
        for i in range(repeat):
            x = self.baseline_x + self.offset_x
            y_start = self.baseline_y + offset_y
            y_end = int(y_start + line_height/5)
            self.draw_it(x, y_start, y_end, DEFENSE_COLOR)

            y_start = int(self.baseline_y + offset_y + line_height * 4/5)
            y_end = self.baseline_y + offset_y + line_height
            self.draw_it(x, y_start, y_end, DEFENSE_COLOR)

            self.offset_x += DEFENSE_X_GAP

    def draw_line_interrupted2(self, offset_y, line_height, line_height_small, repeat):
        for i in range(repeat):
            x = self.baseline_x + self.offset_x
            y_start = self.baseline_y + offset_y
            y_end = int(y_start + line_height * 2/5 + line_height_small)
            self.draw_it(x, y_start, y_end, DEFENSE_COLOR)

            y_start = int(self.baseline_y + offset_y + line_height * 4/5)
            y_end = self.baseline_y + offset_y + line_height
            self.draw_it(x, y_start, y_end, DEFENSE_COLOR)

            self.offset_x += DEFENSE_X_GAP

    def draw_lines_interrupted(self, offset_y, line_height, line_height_small, repeat):
        for i in range(repeat):
            x = self.baseline_x + self.offset_x
            y_start = self.baseline_y + offset_y
            y_end = y_start + int(line_height / 5)
            self.draw_it(x, y_start, y_end, DEFENSE_COLOR)

            y_start = self.baseline_y + offset_y + int(line_height * 2/5)
            y_end = y_start + + line_height_small
            self.draw_it(x, y_start, y_end, DEFENSE_COLOR)

            y_start = self.baseline_y + offset_y + int(line_height * 4/5)
            y_end = self.baseline_y + offset_y + line_height
            self.draw_it(x, y_start, y_end, DEFENSE_COLOR)

            self.offset_x += DEFENSE_X_GAP
