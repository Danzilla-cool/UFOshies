__author__ = 'dany'


class Sprite:
    def __init__(self, xpos, ypos):
        self.forms = []
        self.x = xpos
        self.y = ypos
        self.direction = 1

    def load_png(self, names):
        if len(names) != 4:
            for i in range(4):
                self.forms.append(pygame.image.load(names[0]))
        else:
            for name in names:
                self.forms.append(pygame.image.load(name))
        return self

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

    def set_direction(self, value):
        self.direction = value

        ind = value - 1

        self.bitmap = self.forms[ind]

        self.bitmap.set_colorkey((250, 250, 250))
        return self

    def up(self):
        self.set_direction(4)
        self.y -= self.step

    def right(self):
        self.set_direction(1)
        self.x += self.step

    def down(self):
        self.set_direction(2)
        self.y += self.step

    def left(self):
        self.set_direction(3)
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

