__author__ = 'dany'
from src.classes.sprite import Sprite


class Spaceship(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos)
        self.hp = 10