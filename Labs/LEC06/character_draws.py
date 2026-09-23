# 실습 과제 진행
from pico2d import *

character = load_image('character.png')
open_canvas(800, 600)

def move_circle():
    print("Circle is moving")
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