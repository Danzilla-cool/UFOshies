__author__ = 'dany'
from src.classes.sprite import Sprite


class Projectile(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos)
        self.step = 8
