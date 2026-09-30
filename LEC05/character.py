from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.
frame = 0
character = load_image('run_animation.png')
grass = load_image('grass.png')
for x in range(0, 800, 10):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw( 
        frame * 100, 0,
        100, 100,
        x, 90, #destinaiton x, y
        200, 200 #scale x, y
    )
    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)





delay(2)

close_canvas()

