__author__ = 'dany'
from src.classes.sprite import Sprite


class Bonus(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos)