from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
SCALE = 6
FRAME_TIME = 0.1

# (아래쪽 y, 높이, 프레임 목록)
# 프레임 (x, 너비, 좌우 보정값): y는 pico2d 좌표(아래에서 위로)
ACTIONS = [
    (447, 39, [
        (1, 29, 0), (31, 26, 0), (58, 28, 0), (86, 30, 0), (118, 30, 0), (150, 30, 0),
        (182, 29, 0), (211, 29, 0), (240, 29, 0), (270, 24, 0), (302, 29, 0),
    ]),
    (407, 39, [
        (8, 26, 0), (37, 27, 0), (65, 31, 0), (97, 37, 0), (135, 32, 0), (170, 32, 0),
        (206, 26, 0), (238, 24, 0), (263, 30, 0), (295, 36, 0), (334, 32, 0), (370, 29, 0),
    ]),
]

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
image = load_image('sonic-sprite.png')

running = True
action_index = 1
frame_index = 0
last_time = get_time()
while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    frames = ACTIONS[action_index][2]
    if get_time() - last_time >= FRAME_TIME:
        frame_index = (frame_index + 1) % len(frames)
        last_time = get_time()

    bottom, h, frames = ACTIONS[action_index]
    x, w, dx = frames[frame_index]
    clear_canvas()
    image.clip_draw(x, bottom, w, h,
                    CANVAS_WIDTH // 2 + dx * SCALE, CANVAS_HEIGHT // 2,
                    w * SCALE, h * SCALE)
    update_canvas()
    delay(0.01)

close_canvas()
