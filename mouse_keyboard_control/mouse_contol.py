from pynput.mouse import Controller as mcont
from pynput.keyboard import Controller as kcont
from pynput.mouse import Button
import time
import math
import random

def deg_to_rad(deg):
    rad = deg/57.2957795
    return rad


def move_mouse(angle):
    x_to_move = math.cos(angle) * 10
    y_to_move = math.sin(angle) * 10
    print(x_to_move, y_to_move)
    mouse.move(int(x_to_move), int(y_to_move))


for deg in range(360):
    move_mouse(deg_to_rad(deg*3))


keyboard = kcont()
# keyboard.type('i dont know what to write')

