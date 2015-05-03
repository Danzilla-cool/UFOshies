__author__ = 'dany'
import pygame
from src.classes.spaceship import Spaceship


class Hero(Spaceship):
    def __init__(self, xpos, ypos):
        Spaceship.__init__(self, xpos, ypos)
        self.level = 1
        self.projectiles = 20
        self.step = 10
        self.direction_fire = "fire1"
        self.hp = 10

    def load_png(self, names):
        for i in range(len(names)):
            self.forms.append(pygame.image.load(names[i]))

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

