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

