import math

from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
REPEAT_COUNT = 5
PAUSE_TIME = 1.0
WAIT_STEP = 0.01

# (이름, 프레임 딜레이, 프레임 좌표 목록)
# 프레임 좌표 (x, y, w, h): 시트 이미지의 왼쪽 위 기준
ANIMATIONS = [
    ('idle', 0.12, [
        (1, 39, 29, 39), (31, 40, 26, 38), (58, 39, 28, 39), (86, 40, 30, 38),
        (118, 40, 30, 38), (150, 40, 30, 38), (182, 40, 29, 38),
    ]),
    ('walk', 0.08, [
        (8, 80, 26, 37), (37, 80, 27, 37), (65, 80, 31, 38), (97, 80, 37, 37),
        (135, 80, 32, 35), (170, 79, 32, 38), (206, 79, 26, 38), (238, 80, 24, 37),
        (263, 80, 30, 37), (295, 80, 36, 37), (334, 80, 32, 36), (370, 79, 29, 38),
    ]),
    ('dash', 0.06, [
        (1, 124, 33, 40), (39, 124, 35, 39), (89, 125, 35, 38),
        (130, 121, 34, 42), (181, 122, 34, 41), (228, 122, 33, 40),
    ]),
    ('run', 0.05, [
        (1, 283, 29, 35), (36, 283, 30, 35), (72, 286, 39, 31),
        (123, 285, 39, 32), (172, 286, 39, 31), (218, 285, 38, 32),
    ]),
    ('spin', 0.04, [
        (1, 169, 29, 30), (35, 167, 29, 31), (67, 169, 30, 29),
        (98, 169, 31, 29), (131, 168, 29, 30), (162, 168, 29, 31),
        (193, 170, 30, 29), (230, 170, 31, 29), (268, 170, 30, 30),
    ]),
]

MAX_FRAME_HEIGHT = max(h for _, _, frames in ANIMATIONS for _, _, _, h in frames)
# 가장 큰 프레임이 화면 높이의 절반 이상이 되도록 확대
SCALE = math.ceil(CANVAS_HEIGHT / 2 / MAX_FRAME_HEIGHT)
# 가장 큰 프레임이 화면 세로 중앙에 오도록 바닥 높이 계산
GROUND_Y = (CANVAS_HEIGHT - MAX_FRAME_HEIGHT * SCALE) // 2

running = True
paused = False
skip = False
show_box = False


def handle_events():
    global running, paused, skip, show_box
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_SPACE:
                paused = not paused
            elif event.key == SDLK_RIGHT:
                skip = True
            elif event.key == SDLK_d:
                show_box = not show_box


def wait(seconds):
    elapsed = 0.0
    while elapsed < seconds and running and not skip:
        handle_events()
        delay(WAIT_STEP)
        if not paused:
            elapsed += WAIT_STEP


def draw_frame(x, y, w, h):
    clear_canvas()
    background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, CANVAS_WIDTH, CANVAS_HEIGHT)
    bottom = sheet.h - y - h
    center_x = CANVAS_WIDTH // 2
    center_y = GROUND_Y + h * SCALE // 2
    sheet.clip_draw(x, bottom, w, h, center_x, center_y, w * SCALE, h * SCALE)
    if show_box:
        draw_rectangle(center_x - w * SCALE // 2, GROUND_Y,
                       center_x + w * SCALE // 2, GROUND_Y + h * SCALE)
    update_canvas()


def check_frames():
    for name, _, frames in ANIMATIONS:
        for x, y, w, h in frames:
            assert x + w <= sheet.w and y + h <= sheet.h, f'{name} 프레임이 시트 밖: {(x, y, w, h)}'


def play_animation(name, frames, frame_delay):
    global skip
    skip = False
    print(f'{name}: {len(frames)} frames')
    for _ in range(REPEAT_COUNT):
        for x, y, w, h in frames:
            if not running or skip:
                return
            draw_frame(x, y, w, h)
            wait(frame_delay)
    wait(PAUSE_TIME)


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sheet = load_image('sonic-sprite.png')
background = load_image('TUK_GROUND.png')
check_frames()
print('SPACE: 일시정지, RIGHT: 다음 애니메이션, D: 경계 표시, ESC: 종료')

while running:
    for name, frame_delay, frames in ANIMATIONS:
        play_animation(name, frames, frame_delay)
        if not running:
            break

close_canvas()
