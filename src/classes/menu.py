__author__ = 'dany'
import pygame


''' import my classes '''
from src.classes.ufo import UFO

''' import my utils '''
from src.utils.constants import *


class Menu():
    def __init__(self, punkts):
        self.punkts = punkts
        self.menu_backgroud = pygame.image.load(TEXTURE_PATH + "space3.png").convert()
        self.label_string = pygame.Surface((1200, 200))
        self.label = pygame.font.SysFont("Luminari", 70, True)

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def show(self, screen, window):
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        enemy_picture = UFO(605, 80, step=2)
        enemy_picture.load_png([TEXTURE_PATH + "Alien.png"])
        enemy_picture.set_direction(4)
        done = True
        font_menu = pygame.font.SysFont("Chalkduster", 40)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)

        punkt = 0
        while done:
            # screen.fill((45, 36, 75))
            screen.blit(self.menu_backgroud, (0, 0))
            self.label_string.fill((239, 36, 75))

            mp = pygame.mouse.get_pos()

            for i in self.punkts:
                if i[0] < mp[0] < i[0] + 255 and i[1] < mp[1] - 130 < i[1] + 50:
                    punkt = i[5]
                self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                    if e.key == 13:  # 13 - код enter'а
                        if punkt == 0:
                            done = False
                        elif punkt == 1:
                            exit()

                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        exit()
            enemy_picture.render(screen)

            self.label_string.blit(self.label.render(u"Уфошки", 1, (239, 249, 75)), (480, 30))
            window.blit(self.label_string, (0, 0))
            window.blit(screen, (0, 150))
            pygame.display.flip()
