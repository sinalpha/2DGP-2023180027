from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
SCALE = 6

# (아래쪽 y, 높이, 프레임 목록)
# 프레임 (x, 너비, 좌우 보정값): y는 pico2d 좌표(아래에서 위로)
ACTIONS = [
    (447, 39, [
        (1, 29, 0), (31, 26, 0), (58, 29, 0), (87, 29, 0), (118, 30, 0), (150, 30, 0),
        (182, 29, 0), (211, 29, 0), (240, 29, 0), (270, 24, 0), (302, 29, 0),
    ]),
]

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
image = load_image('sonic-sprite.png')

running = True
action_index = 0
frame_index = 0
while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    bottom, h, frames = ACTIONS[action_index]
    x, w, dx = frames[frame_index]
    clear_canvas()
    image.clip_draw(x, bottom, w, h,
                    CANVAS_WIDTH // 2 + dx * SCALE, CANVAS_HEIGHT // 2,
                    w * SCALE, h * SCALE)
    update_canvas()
    delay(0.01)

close_canvas()
