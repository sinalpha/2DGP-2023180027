from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
SCALE = 6

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
image = load_image('sonic-sprite.png')

running = True
while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    clear_canvas()
    image.clip_draw(1, 447, 29, 39, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
                    29 * SCALE, 39 * SCALE)
    update_canvas()
    delay(0.01)

close_canvas()
