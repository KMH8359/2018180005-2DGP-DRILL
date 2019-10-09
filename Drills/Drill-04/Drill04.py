from pico2d import *


def handle_events():
    global running
    global dir
    global frameY
    global x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if x <= 0:
                    x += 10
                frameY = 100
                dir += 1
            elif event.key == SDLK_LEFT:
                if x >= 800:
                    x -= 10
                frameY = 0
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                 dir += 1



open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frameX = 0
frameY = 100
dir = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frameX * 100, frameY, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frameX = (frameX + 1) % 8

    if x <= 800 and x >= 0:
        x += dir * 5
    delay(0.01)

close_canvas()

