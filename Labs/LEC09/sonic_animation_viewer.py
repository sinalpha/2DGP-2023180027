from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
SCALE = 3
FRAME_TIME = 0.1
REPEAT_COUNT = 5
REST_TIME = 0.5
WRAP_MARGIN = 20 * SCALE

# (아래쪽 y, 높이, 이동 속도, 프레임 목록)
# 이동 속도: 1초에 오른쪽으로 가는 거리(원본 픽셀), 0이면 제자리
# 프레임 (x, 너비, 좌우 보정값): y는 pico2d 좌표(아래에서 위로)
ACTIONS = [
    (447, 39, 0, [
        (1, 29, 0), (31, 26, 0), (58, 28, 0), (86, 30, 1), (118, 30, 2), (150, 30, 2),
        (182, 29, 2), (211, 29, 1), (240, 29, 1), (270, 24, -1), (302, 29, -4),
    ]),
    (407, 39, 40, [
        (8, 26, 0), (37, 27, 1), (65, 31, 2), (97, 37, 2), (135, 32, 1), (170, 32, 3),
        (206, 26, 0), (238, 24, 0), (263, 30, 1), (295, 36, 0), (334, 32, -1), (370, 29, -3),
    ]),
    (361, 43, 60, [
        (1, 33, 0), (39, 35, -2), (89, 35, -1), (130, 34, -1), (181, 34, 4), (228, 33, 6),
    ]),
    (325, 33, 100, [
        (1, 29, 0), (35, 29, 0), (67, 30, 0), (98, 31, 0), (131, 29, 0), (162, 29, 0),
        (193, 30, 0), (230, 31, 0), (268, 30, 0),
    ]),
    (292, 27, 100, [
        (1, 30, 0), (36, 29, 0), (70, 29, 0), (105, 29, 0), (139, 29, 0), (174, 29, 0),
    ]),
    (251, 36, 100, [
        (1, 29, 0), (36, 30, -1), (74, 31, -2), (111, 31, -2), (149, 30, -2), (186, 31, -2),
    ]),
    (207, 35, 140, [
        (1, 29, 0), (36, 30, -1), (72, 39, -2), (123, 39, -2), (172, 39, -2), (218, 38, -1),
    ]),
    (154, 45, 0, [
        (1, 24, 0), (31, 29, 1), (65, 20, 1), (90, 25, 4), (119, 25, -3), (149, 20, 0),
        (184, 40, 2), (232, 39, 2),
    ]),
    (108, 40, 0, [
        (1, 27, 0), (31, 31, 3), (64, 31, 2), (99, 33, 0), (136, 32, 1), (176, 33, 0),
        (217, 33, 1), (254, 33, 0),
    ]),
    (56, 43, 0, [
        (6, 34, 0), (49, 34, 0), (96, 23, -1), (125, 23, -1),
    ]),
]


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update():
    global action_index, frame_index, repeat, resting, last_time
    global x_pos, move_time
    speed, frames = ACTIONS[action_index][2:]
    if not resting:
        x_pos += speed * SCALE * (get_time() - move_time)
        if x_pos > CANVAS_WIDTH + WRAP_MARGIN:
            x_pos -= CANVAS_WIDTH + 2 * WRAP_MARGIN
    move_time = get_time()

    if resting:
        if get_time() - last_time >= REST_TIME:
            action_index = (action_index + 1) % len(ACTIONS)
            frame_index = 0
            repeat = 0
            resting = False
            x_pos = CANVAS_WIDTH // 2
            last_time = get_time()
    elif get_time() - last_time >= FRAME_TIME:
        frame_index += 1
        if frame_index >= len(frames):
            repeat += 1
            if repeat < REPEAT_COUNT:
                frame_index = 0
            else:
                frame_index = len(frames) - 1
                resting = True
        last_time = get_time()


def draw():
    bottom, h, speed, frames = ACTIONS[action_index]
    x, w, dx = frames[frame_index]
    clear_canvas()
    image.clip_draw(x, bottom, w, h,
                    int(x_pos) + dx * SCALE, CANVAS_HEIGHT // 2,
                    w * SCALE, h * SCALE)
    update_canvas()


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
image = load_image('sonic-sprite.png')

running = True
action_index = 0
frame_index = 0
repeat = 0
resting = False
x_pos = CANVAS_WIDTH // 2
last_time = get_time()
move_time = get_time()
while running:
    handle_events()
    update()
    draw()
    delay(0.01)

close_canvas()
