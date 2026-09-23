# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)


character = load_image('character.png')

CENTER_X, CENTER_Y = 400, 300
SIZE = 100

def move_circle():
    print("Circle is moving")
    for angle in range(0, 360, 2):
        rad = math.radians(angle)
        x = CENTER_X + SIZE * math.cos(rad)
        y = CENTER_Y + SIZE * math.sin(rad)
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)

def move_rectangle():
    print("Rectangle is moving")
    corners = [
        (CENTER_X - SIZE, CENTER_Y - SIZE),
        (CENTER_X + SIZE, CENTER_Y - SIZE),
        (CENTER_X + SIZE, CENTER_Y + SIZE),
        (CENTER_X - SIZE, CENTER_Y + SIZE),
        (CENTER_X - SIZE, CENTER_Y - SIZE),
    ]
    steps_per_side = 30
    for i in range(len(corners) - 1):
        x1, y1 = corners[i]
        x2, y2 = corners[i + 1]

def move_triangle():
    print("Triangle is moving")
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()