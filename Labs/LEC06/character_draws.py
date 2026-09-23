# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)


character = load_image('character.png')

CENTER_X, CENTER_Y = 400, 300
SIZE = 100

def move_circle():
    print("Circle is moving")
    angle = 0
    rad = math.radians(angle)
    x = CENTER_X + SIZE * math.cos(rad)
    y = CENTER_Y + SIZE * math.sin(rad)
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    pass

def move_rectangle():
    print("Rectangle is moving")
    pass

def move_triangle():
    print("Triangle is moving")
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()