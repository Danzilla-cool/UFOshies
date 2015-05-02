__author__ = 'dany'
from src.classes.spaceship import Spaceship


class Hero(Spaceship):
    def __init__(self, xpos, ypos):
        Spaceship.__init__(self, xpos, ypos)
        self.level = 1
        self.projectiles = 20
        self.step = 10
