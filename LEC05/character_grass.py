from pico2d import *
from math import *

dir = 0

padding_x = 50
padding_y = 50
x = padding_x
y = padding_y;
theta = 0;

def update():
    global x, y, dir, theta
    center_x = 800 / 2
    center_y = 600 / 2
    r = 100
    x = center_x + r * cos(theta)
    y = center_y + r * sin(theta)
    theta += 0.01


# def update():
#     global x, y, dir
#     if dir == 0:
#         x += 2
#         if x >= 800 - padding_x:
#             dir = 1
#             x, y = 800 - padding_x, 0 + padding_y
#     elif dir == 1:
#         y += 2
#         if(y >= 600 - padding_y):
#             dir = 2
#             x, y = 800 - padding_x, 600 - padding_y
#     elif dir == 2:
#         x -= 2
#         if(x <= 0 + padding_x):
#             dir = 3
#             x, y = 0 + padding_x, 600 - padding_y
#     elif dir == 3:
#         y -= 2
#         if(y <= 0 + padding_y):
#             dir = 0
#             x, y = 0 + padding_x, 0 + padding_y

def draw():
    global x, y, dir
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    pass

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')


# 0 right 1 up 2 left 3 down

while True:

    update()
    draw()


    delay(0.01)



close_canvas()