# # 실습 과제 진행
from pico2d import *
# import math

open_canvas(800, 600)

character = load_image('character.png')

CENTER_X, CENTER_Y = 400, 300
SIZE = 100
# running = True

# def handle_events():
#     global running
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             running = False

def render_frame(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_line(x1, y1, x2, y2, steps):
    for step in range(steps):
        t = step / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        render_frame(x, y)

# def move_along_path(corners, steps_per_side):
#     for i in range(len(corners) - 1):
#         x1, y1 = corners[i]
#         x2, y2 = corners[i + 1]
#         for step in range(steps_per_side):
#             if not running:
#                 return
#             t = step / steps_per_side
#             x = x1 + (x2 - x1) * t
#             y = y1 + (y2 - y1) * t
#             render_frame(x, y)


def move_circle():
    print("Circle is moving")
    for angle in range(0, 360, 2):
#     #     if not running:
#     #         return
        rad = math.radians(angle)
        x = CENTER_X + SIZE * math.cos(rad)
        y = CENTER_Y + SIZE * math.sin(rad)
        render_frame(x, y)

def move_rectangle():
    print("Rectangle is moving")
#     # corners = [
#     #     (CENTER_X - SIZE, CENTER_Y - SIZE),
#     #     (CENTER_X + SIZE, CENTER_Y - SIZE),
#     #     (CENTER_X + SIZE, CENTER_Y + SIZE),
#     #     (CENTER_X - SIZE, CENTER_Y + SIZE),
#     #     (CENTER_X - SIZE, CENTER_Y - SIZE),
#     # ]
    move_top_left_to_top_right()
    move_top_right_to_bottom_right()
    move_bottom_right_to_bottom_left()
    move_bottom_left_to_top_left()
#     # move_along_path(corners, steps_per_side=30)

RECT_LEFT, RECT_RIGHT = 20, 780
RECT_BOTTOM, RECT_TOP = 40, 550
RECTANGLE_STEPS = 40

def move_top_left_to_top_right():
    for x in range(0, 780, 2):
        render_frame(x, 550)
    pass

def move_top_right_to_bottom_right():
    for y in range(550, 40, -2):
        render_frame(780, y)
    pass

def move_bottom_right_to_bottom_left():
    for x in range(780, 0, -2):
        render_frame(x, 40)
    pass

def move_bottom_left_to_top_left():
    for y in range(40, 550, 2):
        render_frame(20, y)
    pass

def move_triangle():
    print("Triangle is moving")
    move_top_to_bottom_left()
    move_bottom_left_to_bottom_right()
    move_bottom_right_to_top()
#     # corners = [
#     #     (CENTER_X, CENTER_Y + SIZE),
#     #     (CENTER_X + SIZE, CENTER_Y - SIZE),
#     #     (CENTER_X - SIZE, CENTER_Y - SIZE),
#     #     (CENTER_X, CENTER_Y + SIZE),
#     # ]
#     # move_along_path(corners, steps_per_side=40)

TOP_X, TOP_Y = CENTER_X, CENTER_Y + SIZE
LEFT_X, LEFT_Y = CENTER_X - SIZE, CENTER_Y - SIZE
RIGHT_X, RIGHT_Y = CENTER_X + SIZE, CENTER_Y - SIZE
TRIANGLE_STEPS = 40

def move_top_to_bottom_left():
    move_line(TOP_X, TOP_Y, LEFT_X, LEFT_Y, TRIANGLE_STEPS)

def move_bottom_left_to_bottom_right():
    move_line(LEFT_X, LEFT_Y, RIGHT_X, RIGHT_Y, TRIANGLE_STEPS)

def move_bottom_right_to_top():
    move_line(RIGHT_X, RIGHT_Y, TOP_X, TOP_Y, TRIANGLE_STEPS)

while True:
    print("Game Loop Start")
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()