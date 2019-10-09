from pico2d import *



KPU_WIDTH, KPU_HEIGHT = 1280, 1024





def handle_events():

    global running

    global process

    global x, y

    global dirX, dirY

    global charX, charY

    global chardir

    events = get_events()

    for event in events:

        if event.type == SDL_QUIT:

            process = False

        elif event.type == SDL_MOUSEMOTION:

            x, y = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:

            process = False

        elif event.type == SDL_MOUSEBUTTONDOWN:

            if running == False:

                running = True
                
            dirX, dirY = event.x - 20, KPU_HEIGHT - 1 - event.y + 20

            if dirX < charX:

                chardir = 0

            elif dirX > charX:

                chardir = 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')

character = load_image('animation_sheet.png')

cursor = load_image('hand_arrow.png')



running = False

process = True

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

dirX, dirY = 0, 0

charX, charY = KPU_WIDTH // 2, KPU_HEIGHT // 2

frame = 0

chardir = 1

hide_cursor()



while process:

    clear_canvas()

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    cursor.draw(x,y)

    if dirX:

        if dirX == charX and dirY == charY:

            dirX = 0

            dirY = 0

        charX += (dirX - charX) / 100

        charY += (dirY - charY) / 100

    character.clip_draw(frame * 100, 100 * chardir, 100, 100, charX, charY)

    update_canvas()

    frame = (frame + 1) % 8



    handle_events()



close_canvas()
