from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
SHEET_HEIGHT = 525
SCALE = 8
GROUND_Y = 140
REPEAT_COUNT = 5
PAUSE_TIME = 1.0
FRAME_DELAY = 0.08

# 프레임 좌표 (x, y, w, h): 시트 이미지의 왼쪽 위 기준
ANIMATIONS = [
    ('idle', [
        (1, 39, 29, 39), (31, 40, 26, 38), (58, 39, 28, 39), (86, 40, 30, 38),
        (118, 40, 30, 38), (150, 40, 30, 38), (182, 40, 29, 38),
    ]),
    ('walk', [
        (8, 80, 26, 37), (37, 80, 27, 37), (65, 80, 31, 38), (97, 80, 37, 37),
        (135, 80, 32, 35), (170, 79, 32, 38), (206, 79, 26, 38), (238, 80, 24, 37),
        (263, 80, 30, 37), (295, 80, 36, 37), (334, 80, 32, 36), (370, 79, 29, 38),
    ]),
    ('dash', [
        (1, 124, 33, 40), (39, 124, 35, 39), (89, 125, 35, 38),
        (130, 121, 34, 42), (181, 122, 34, 41), (228, 122, 33, 40),
    ]),
    ('run', [
        (1, 283, 29, 35), (36, 283, 30, 35), (72, 286, 39, 31),
        (123, 285, 39, 32), (172, 286, 39, 31), (218, 285, 38, 32),
    ]),
    ('spin', [
        (1, 169, 29, 30), (35, 167, 29, 31), (67, 169, 30, 29),
        (98, 169, 31, 29), (131, 168, 29, 30), (162, 168, 29, 31),
        (193, 170, 30, 29), (230, 170, 31, 29), (268, 170, 30, 30),
    ]),
]

running = True


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_frame(x, y, w, h):
    clear_canvas()
    bottom = SHEET_HEIGHT - y - h
    sheet.clip_draw(x, bottom, w, h,
                    CANVAS_WIDTH // 2, GROUND_Y + h * SCALE // 2,
                    w * SCALE, h * SCALE)
    update_canvas()


def play_animation(frames):
    for _ in range(REPEAT_COUNT):
        for x, y, w, h in frames:
            draw_frame(x, y, w, h)
            delay(FRAME_DELAY)
    delay(PAUSE_TIME)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sheet = load_image('sonic-sprite.png')

while True:
    for name, frames in ANIMATIONS:
        play_animation(frames)

close_canvas()
