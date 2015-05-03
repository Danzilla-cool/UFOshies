__author__ = 'dany'
from src.classes.spaceship import Spaceship
import pygame
from src.utils.constants import *
import random

class UFO(Spaceship):
    def __init__(self, xpos, ypos, step):
        Spaceship.__init__(self, xpos, ypos)
        self.step = step
        self.hp = random.randint(ufo_min_hp, ufo_max_hp)
        self.max_hp = self.hp

    def load_png(self, names):
        for i in range(len(names)):
            self.forms.append(pygame.image.load(names[i]))

    def update(self):
        if self.hp < self.max_hp * (1 / 3):
            self.bitmap = self.forms[2]
        elif self.hp < self.max_hp * (2 / 3):
            self.bitmap = self.forms[1]
        else:
            self.bitmap = self.forms[0]