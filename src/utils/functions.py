__author__ = 'dany'
import random
import platform
from src.utils.constants import *


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

def get_delay():
    delay = 0
    os = platform.system()

    if os == "Windows":
        delay = WINDOWS_DELAY
    elif os == "Darwin":
        delay = MACOS_DELAY
    elif os == "Linux":
        delay = LINUX_DELAY
    return delay