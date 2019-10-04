from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frameX = 0
frameY = 100
movement = 40

while (True):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frameX * 100, frameY, 100, 100, x, 90)
    update_canvas()

    frameX = (frameX + 1) % 8 
    x += movement

    delay(0.05)
    get_events()

    if (x >= 800):
        frameY = 0
        movement = -40

    if (x <= 0):
        frameY = 100
        movement = 40

close_canvas()

