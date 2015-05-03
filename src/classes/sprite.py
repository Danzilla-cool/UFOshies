__author__ = 'dany'
import pygame

class Sprite:
    def __init__(self, xpos, ypos):
        self.forms = []
        self.x = xpos
        self.y = ypos
        self.direction = 1
        self.direction_fire = "fire1"

    def load_png(self, names):
        if len(names) == 4:
            for i in range(len(names)):
                self.forms.append(pygame.image.load(names[i]))
        elif len(names) == 1:
            self.forms.append(pygame.image.load(names[0]))
        return self

    def render(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))

    def set_direction(self, value):
        if type(value) == int:
            if len(self.forms) > 1:
                self.direction = value

                ind = value - 1

                self.bitmap = self.forms[ind]

            else:
                self.bitmap = self.forms[0]
        elif type(value) == str:
            if value == "fire1":
                self.bitmap = self.forms[4]
            elif value == "fire2":
                self.bitmap = self.forms[5]
            elif value == "fire3":
                self.bitmap = self.forms[6]
            elif value == "fire4":
                self.bitmap = self.forms[7]
        self.bitmap.set_colorkey((250, 250, 250))
        return self

    def up(self):
        self.direction = 4
        self.set_direction("fire4")
        self.y -= self.step

    def right(self):
        self.direction = 1
        self.set_direction("fire1")
        self.x += self.step

    def down(self):
        self.direction = 2
        self.set_direction("fire2")
        self.y += self.step

    def left(self):
        self.direction = 3
        self.set_direction("fire3")
        self.x -= self.step

    def move(self):
        if self.direction == 1:
            self.right()
        elif self.direction == 2:
            self.down()
        elif self.direction == 3:
            self.left()
        else:
            self.up()


