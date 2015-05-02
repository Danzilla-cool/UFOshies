__author__ = 'dany'
from src.classes.spaceship import Spaceship


class UFO(Spaceship):
    def __init__(self, xpos, ypos, step):
        Spaceship.__init__(self, xpos, ypos)
        self.step = step
