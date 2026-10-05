from pico2d import *

open_canvas(800, 600)
image = load_image('sonic-sprite.png')

clear_canvas()
image.draw(400, 300)
update_canvas()
delay(2)

close_canvas()
