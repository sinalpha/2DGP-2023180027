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


def draw_frame(row, frame):
    clear_canvas()
    left = frame * CELL_SIZE
    bottom = SHEET_HEIGHT - (row + 1) * CELL_SIZE
    sheet.clip_draw(left, bottom, CELL_SIZE, CELL_SIZE,
                    CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
                    CELL_SIZE * SCALE, CELL_SIZE * SCALE)
    update_canvas()


def play_animation(row, frame_count):
    for _ in range(REPEAT_COUNT):
        for frame in range(frame_count):
            draw_frame(row, frame)
            delay(FRAME_DELAY)
    delay(PAUSE_TIME)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sheet = load_image('SamuraiSheet.png')

close_canvas()
