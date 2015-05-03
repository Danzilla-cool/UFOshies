__author__ = 'dany'
import time
import pygame
import math

''' import my classes '''
from src.classes.sprite import Sprite
from src.classes.ufo import UFO
from src.classes.hero import Hero
from src.classes.menu import Menu
from src.classes.bonus import Bonus

''' import my utils '''
from src.utils.functions import *
from src.utils.constants import *

if __name__ == '__main__':

    file = open("record.txt", "r+")
    arr = file.readlines()

    ''' Creating window '''
    window = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("UFOshes")

    screen = pygame.Surface((1200, 700))
    background_image = pygame.image.load(TEXTURE_PATH + "space2.jpg").convert()

    info_string = pygame.Surface((1200, 50))

    count = 0
    spawn_level = 40
    bonus_level = 70
    spawn = 0
    enemies_step = 2

    hero_moving = False

    ufo_min_hp = 3
    ufo_max_hp = 6

    projectiles_arr = []
    enem_arr = []
    bonus_arr = []

    punkts = [(510, 300, "Start Game", (250, 250, 30), (250, 30, 250), 0),
              (560, 350, "Quit", (250, 250, 30), (250, 30, 250), 1)]

    pygame.font.init()

    projectil_inf = pygame.font.SysFont("Apple Chancery", 32)
    killed_inf = pygame.font.SysFont("Braggadocio", 32, True, True)
    hp_inf = pygame.font.SysFont("Chalkduster", 32, True, True)
    label_font = pygame.font.SysFont("Luminari", 45, True, True)
    game_over_string = pygame.Surface((1200, 100))
    game_over_font = pygame.font.SysFont(None, 55, True, True)

    menu = Menu(punkts)
    menu.show(screen, window)

    hero = Hero(xpos=600, ypos=300).load_png(
        [TEXTURE_PATH + "sh1.png", TEXTURE_PATH + "sh2.png", TEXTURE_PATH + "sh3.png", TEXTURE_PATH + "sh4.png"])
    hero.set_direction(random.randint(0, 3))
    hero.step = 4

    pygame.key.set_repeat(1, 1)
    projectile_step = 12
    projectiles = 20
    once = True
    pygame.key.set_repeat(1, 1)
    pygame.mouse.set_visible(False)
    done = True
    chiter = False
    label_color = 0
    while done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            if e.type == pygame.KEYDOWN:
                if (e.key == pygame.K_UP or e.key == pygame.K_w or e.key == 172) and hero.y > 0:
                    hero_moving = True
                    spawn += 1
                    hero.up()

                if (e.key == pygame.K_DOWN or e.key == pygame.K_s or e.key == 161) and hero.y < 700 - hero.step:
                    hero_moving = True
                    spawn += 1
                    hero.down()

                if (e.key == pygame.K_LEFT or e.key == pygame.K_a or e.key == 160) and hero.x > 0:
                    hero_moving = True
                    spawn += 1
                    hero.left()

                if (e.key == pygame.K_RIGHT or e.key == pygame.K_d or e.key == 162) and hero.x < 1100 - hero.step:
                    hero_moving = True
                    spawn += 1
                    hero.right()

                if e.key == pygame.K_h:
                    if not chiter:
                        hero.step += 30
                        projectile_step += 30
                        chiter = True
                    else:
                        hero.step -= 30
                        projectile_step -= 30
                        chiter = False

                if e.key == pygame.K_ESCAPE:
                    menu.show(screen, window)
                    pygame.key.set_repeat(1, 1)
                    pygame.mouse.set_visible(False)

                if e.key == pygame.K_SPACE:
                    if projectiles > 0:
                        projectiles -= 1

                        new_projectile = Sprite(hero.x + 52, hero.y + 52).load_png(
                            [TEXTURE_PATH + "proj1.png", TEXTURE_PATH + "proj2.png", TEXTURE_PATH + "proj3.png",
                             TEXTURE_PATH + "proj4.png"])

                        new_projectile.set_direction(hero.direction)
                        new_projectile.in_label = True
                        projectiles_arr.append(new_projectile)


        # screen.fill((62, 15, 255))
        screen.blit(background_image, [0, 0])
        info_string.fill((172, 212, 33))

        for enemy in enem_arr:
            if hero.x > enemy.x:
                enemy.x += enemy.step
            else:
                enemy.x -= enemy.step

            if hero.y > enemy.y:
                enemy.y += enemy.step
            else:
                enemy.y -= enemy.step

        if spawn == spawn_level or once:
            e_x, e_y = get_random_coordinates(1200, 700, 50, 50, 10)
            new_enemy = UFO(e_x, e_y, enemies_step).load_png([TEXTURE_PATH + "Alien.png"])
            new_enemy.set_direction(hero.direction)
            new_enemy.hp = random.randint(ufo_min_hp, ufo_max_hp)
            enem_arr.append(new_enemy)
            spawn = 0
            once = False

        m = 0
        while m < len(bonus_arr):
            bon = bonus_arr[m][0]
            bon.set_direction(4)
            bon.render(screen)
            if intersect(hero.x, bon.x, hero.y, bon.y, 100, 100, 50, 100):
                hero.hp += 2
                if hero.hp > 10:
                    hero.hp = 10
                projectiles += 5
                del bonus_arr[m]
            else:
                bonus_arr[m][1] += 1
                if bonus_arr[m][1] > bonus_level:
                    del bonus_arr[m]
            m += 1

        j = 0
        while j < len(enem_arr):
            enemy = enem_arr[j]
            enemy.render(screen)
            if intersect(hero.x, enemy.x, hero.y, enemy.y, 90, 90, 80, 80):
                hero.hp -= 1
                enemy.hp -= 2

                if enemy.hp <= 0:
                    del enem_arr[j]
                    count += 1
                    projectiles += random.randint(1, 5)

                if hero.hp <= 0:
                    file.write(str(count) + "\n")
                    window.blit(info_string, (0, 0))
                    projectiles_arr = []
                    enem_arr = []
                    pygame.key.set_repeat(1, 1)

                    game_over_string.fill((50, 50, 50))
                    game_over_string.blit(game_over_font.render(u"GAME OVER", 1, (245, 36, 75)), (450, 35))
                    window.blit(game_over_string, (0, 350))
                    pygame.display.flip()

                    info_string.blit(killed_inf.render(u"Count: " + str(count), 1, (147, 61, 255)), (175, 15))
                    info_string.blit(projectil_inf.render(u"Projectiles: " + str(projectiles), 1, (62, 61, 255)),
                                     (800, -5))
                    info_string.blit(label_font.render(u"Уфошки", 1, (label_color, 50, 200)), (500, -9))
                    info_string.blit(hp_inf.render(u"HP: " + str(hero.hp), 1, (250, 50, 0)), (1025, 5))

                    window.blit(info_string, (0, 0))
                    pygame.display.flip()
                    hero.hp = 10
                    count = 0
                    projectiles = 10
                    spawn = 0

                    time.sleep(2)

                    menu.show(screen, window)

                    pygame.key.set_repeat(1, 1)
                    pygame.mouse.set_visible(False)
                    break
            j += 1

        i = 0
        while i < len(projectiles_arr):
            projectile = projectiles_arr[i]
            if projectile.in_label:
                projectile.render(screen)
                k = 0
                while k < len(enem_arr):
                    enemy = enem_arr[k]
                    if intersect(projectile.x, enemy.x, projectile.y, enemy.y, 20, 100, 50, 90):
                        enemy.hp -= 1
                        try:
                            del projectiles_arr[i]
                        except IndexError:
                            print(i, projectiles_arr)
                            exit()
                        if enemy.hp == 0:
                            if (count + 1) % 10 == 0:
                                enemies_step += 0.1
                                hero.level += 1
                                hero.step += 1
                                ufo_min_hp, ufo_max_hp = ufo_min_hp + 1, ufo_max_hp + 1

                            count += 1
                            projectiles += random.randint(5, 7)
                            del enem_arr[k]
                    k += 1
                if projectile.direction == 1:
                    projectile.x += projectile_step
                elif projectile.direction == 2:
                    projectile.y += projectile_step
                elif projectile.direction == 3:
                    projectile.x -= projectile_step
                elif projectile.direction == 4:
                    projectile.y -= projectile_step

            if projectile.x < 0 or projectile.y < 0 or projectile.x > 1190 or projectile.y > 690:
                projectile.in_label = False
            i += 1

        if hero.x < 10:
            hero.x = 1060
        elif hero.x > 1060:
            hero.x = 10

        if hero.y < 10:
            hero.y = 530
        elif hero.y > 540:
            hero.y = 10

        rand = random.randint(1, 100)
        if rand == 1:
            new_x, new_y = get_random_coordinates(1200, 700, 600, 350, 70)
            new_bonus = Bonus(new_x, new_y)
            new_bonus.load_png([TEXTURE_PATH + "plus.png"])
            bonus_arr.append([new_bonus, 0])

        label_color += 1
        if label_color > 255:
            label_color = 50

        hero.render(screen)
        info_string.blit(killed_inf.render(u"Count: " + str(count), 1, (147, 61, 255)), (175, 15))
        info_string.blit(projectil_inf.render(u"Projectiles: " + str(projectiles), 1, (62, 61, 255)), (800, -5))
        info_string.blit(label_font.render(u"Уфошки", 1, (label_color, 50, 200)), (500, -9))
        info_string.blit(hp_inf.render(u"HP: " + str(hero.hp), 1, (250, 50, 0)), (1025, 5))

        window.blit(info_string, (0, 0))
        window.blit(screen, (0, 50))
        pygame.display.flip()

        pygame.time.delay(100)