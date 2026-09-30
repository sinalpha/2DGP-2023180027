from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
CELL_SIZE = 128
SHEET_HEIGHT = 1280
SCALE = 4
REPEAT_COUNT = 5
PAUSE_TIME = 1.0
FRAME_DELAY = 0.08

ANIMATIONS = [
    ('idle', 0, 6),
    ('walk', 1, 8),
    ('run', 2, 8),
    ('jump', 3, 12),
    ('attack1', 4, 6),
    ('attack2', 5, 4),
    ('attack3', 6, 3),
]
