# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)


character = load_image('character.png')

CENTER_X, CENTER_Y = 400, 300
SIZE = 100

def move_circle():
    print("Circle is moving")
    clear_canvas()
    character.draw(400, 300)
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