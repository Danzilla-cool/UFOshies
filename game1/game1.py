__author__ = 'dany'
import pygame
import random
import time
import math

file = open("record.txt", "r+")
arr = file.readlines()

''' Создание окна '''
window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("UFOformses")

screen = pygame.Surface((1200, 700))
background_image = pygame.image.load("space2.jpg").convert()

info_string = pygame.Surface((1200, 50))

enemies_step = 2


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


class Spaceformsip(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos)
        self.hp = 10


class Hero(Spaceformsip):
    def __init__(self, xpos, ypos):
        Spaceformsip.__init__(self, xpos, ypos)
        self.level = 1
        self.projectiles = 20
        self.step = 10


class UFO(Spaceformsip):
    def __init__(self, xpos, ypos):
        Spaceformsip.__init__(self, xpos, ypos)
        self.step = enemies_step


class Projectile(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos)
        self.step = 8


def intersect(x1, x2, y1, y2, q1, q2, q3, q4):
    if (x1 > x2 - q1) and (x1 < x2 + q2) and (y1 > y2 - q3) and (y1 < y2 + q4):
        return True
    else:
        return False


def get_random_coordinates(Dx, Dy, levelx, levely, o):
    zones = random.choice([True, False])  # В 1 и 2 или 3 и 4 зоне будет
    if zones:
        zone = random.choice([1, 2])  # В 1 или 2 зоне
        if zone == 1:
            x_res = random.randint(o, levelx)
            y_res = random.randint(levely, Dy - levely)
        else:
            x_res = random.randint(Dx - levelx, Dx - o)
            y_res = random.randint(levely, Dy - levely)
    else:
        zone = random.choice([3, 4])
        if zone == 3:
            x_res = random.randint(o, Dx - o)
            y_res = random.randint(o, levely)
        else:
            x_res = random.randint(o, Dx)
            y_res = random.randint(Dy - levely, Dy - o)

    return [x_res, y_res]


class Menu():
    def __init__(self, punkts):
        self.punkts = punkts
        self.menu_backgroud = pygame.image.load("space3.png").convert()
        self.label_string = pygame.Surface((1200, 200))
        self.label = pygame.font.SysFont("Luminari", 70, True)

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        enemy_picture = UFO(605, 80)
        enemy_picture.load_png(["Alien.png"])
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
                        game.menu()
                        pygame.key.set_repeat(1, 1)
                        pygame.mouse.set_visible(False)
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
            enemy_picture.render()

            self.label_string.blit(self.label.render(u"Уфошки", 1, (239, 249, 75)), (480, 30))
            window.blit(self.label_string, (0, 0))
            window.blit(screen, (0, 150))
            pygame.display.flip()


class Bonus(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self, xpos, ypos)


count = 0
spawn_level = 40
bonus_level = 70
spawn = 0

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

game = Menu(punkts)
game.menu()

hero = Hero(xpos=600, ypos=300).load_png(["sh1.png", "sh2.png", "sh3.png", "sh4.png"])
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
                spawn += 1
                hero.up()

            if (e.key == pygame.K_DOWN or e.key == pygame.K_s or e.key == 161) and hero.y < 700 - hero.step:
                spawn += 1
                hero.down()

            if (e.key == pygame.K_LEFT or e.key == pygame.K_a or e.key == 160) and hero.x > 0:
                spawn += 1
                hero.left()

            if (e.key == pygame.K_RIGHT or e.key == pygame.K_d or e.key == 162) and hero.x < 1100 - hero.step:
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
                game.menu()
                pygame.key.set_repeat(1, 1)
                pygame.mouse.set_visible(False)

            if e.key == pygame.K_SPACE:
                if projectiles > 0:
                    projectiles -= 1

                    new_projectile = Sprite(hero.x + 52, hero.y + 52).load_png(
                        ["proj1.png", "proj2.png", "proj3.png", "proj4.png"])

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
        new_enemy = UFO(e_x, e_y).load_png(["Alien.png"])
        new_enemy.set_direction(hero.direction)
        new_enemy.hp = random.randint(ufo_min_hp, ufo_max_hp)
        enem_arr.append(new_enemy)
        spawn = 0
        once = False

    m = 0
    while m < len(bonus_arr):
        bon = bonus_arr[m][0]
        bon.set_direction(4)
        bon.render()
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
        enemy.render()
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
                info_string.blit(projectil_inf.render(u"Projectiles: " + str(projectiles), 1, (62, 61, 255)), (800, -5))
                info_string.blit(label_font.render(u"Spaceformsips", 1, (0, 50, 200)), (500, 10))
                info_string.blit(hp_inf.render(u"HP: " + str(hero.hp), 1, (250, 50, 0)), (1025, 5))

                window.blit(info_string, (0, 0))
                pygame.display.flip()
                hero.hp = 10
                count = 0
                projectiles = 10
                spawn = 0

                time.sleep(2)

                game.menu()

                pygame.key.set_repeat(1, 1)
                pygame.mouse.set_visible(False)
                break
        j += 1

    i = 0
    while i < len(projectiles_arr):
        projectile = projectiles_arr[i]
        if projectile.in_label:
            projectile.render()
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
        new_bonus.load_png(["plus.png"])
        bonus_arr.append([new_bonus, 0])

    label_color += 1
    if label_color > 255:
        label_color = 50

    hero.render()
    info_string.blit(killed_inf.render(u"Count: " + str(count), 1, (147, 61, 255)), (175, 15))
    info_string.blit(projectil_inf.render(u"Projectiles: " + str(projectiles), 1, (62, 61, 255)), (800, -5))
    info_string.blit(label_font.render(u"Уфошки", 1, (label_color, 50, 200)), (500, -9))
    info_string.blit(hp_inf.render(u"HP: " + str(hero.hp), 1, (250, 50, 0)), (1025, 5))

    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 50))
    pygame.display.flip()
