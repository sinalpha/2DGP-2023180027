from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.
frame = 0
action = 0
character = load_image('animation_sheet.png')
grass = load_image('grass.png')



while True:

    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_composite_draw( 
            frame * 100, 0,
            100, 100,
            0, 'h',
            x, 90,
            200, 200
        )
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

    for x in range(800, 0, -10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_composite_draw( 
            frame * 100, action * 100,
            100, 100,
            0, 'h',
            x, 90,
            200, 200
        )
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

    action = (action + 1) % 4




delay(2)
close_canvas()
