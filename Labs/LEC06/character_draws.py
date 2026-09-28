# # 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

CENTER_X, CENTER_Y = 400, 300
SIZE = 100
running = True
FRAME_DELAY = 0.01

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def render_frame(x, y):
    handle_events()
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)

def move_line(x1, y1, x2, y2, steps):
    for step in range(steps):
        if not running:
            return
        t = step / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        render_frame(x, y)

def move_polygon(points, steps):
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        move_line(x1, y1, x2, y2, steps)

CIRCLE_ANGLE_STEP = 2

def move_circle():
    for angle in range(0, 360, CIRCLE_ANGLE_STEP):
        if not running:
            return
        rad = math.radians(angle)
        x = CENTER_X + SIZE * math.cos(rad)
        y = CENTER_Y + SIZE * math.sin(rad)
        render_frame(x, y)

RECT_LEFT, RECT_RIGHT = 20, 780
RECT_BOTTOM, RECT_TOP = 40, 550
RECTANGLE_STEPS = 40

def move_rectangle():
    rectangle = [
        (RECT_LEFT, RECT_TOP),
        (RECT_RIGHT, RECT_TOP),
        (RECT_RIGHT, RECT_BOTTOM),
        (RECT_LEFT, RECT_BOTTOM),
    ]
    move_polygon(rectangle, RECTANGLE_STEPS)

TOP_X, TOP_Y = CENTER_X, CENTER_Y + SIZE
LEFT_X, LEFT_Y = CENTER_X - SIZE, CENTER_Y - SIZE
RIGHT_X, RIGHT_Y = CENTER_X + SIZE, CENTER_Y - SIZE
TRIANGLE_STEPS = 40

def move_triangle():
    triangle = [
        (TOP_X, TOP_Y),
        (LEFT_X, LEFT_Y),
        (RIGHT_X, RIGHT_Y),
    ]
    move_polygon(triangle, TRIANGLE_STEPS)

while running:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()