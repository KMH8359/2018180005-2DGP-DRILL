from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER,START_DASH,START_DASH2,STOP_DASH,STOP_DASH2,STOP_TIMER = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): START_DASH,
    (SDL_KEYDOWN, SDLK_RSHIFT): START_DASH2,
    (SDL_KEYUP, SDLK_LSHIFT): STOP_DASH,
    (SDL_KEYUP, SDLK_RSHIFT): STOP_DASH2,
}



# Boy States
class IdleState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 1000
        
    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)
class RunState:
    @staticmethod
    def enter(boy, event):
        if event == STOP_DASH or event == STOP_DASH2 or event == STOP_TIMER:
            if boy.velocity != 1 and boy.velocity != -1:
                boy.velocity /= 2
        if event == RIGHT_DOWN:
            boy.velocity += 1
            if boy.velocity > 1:
                boy.velocity = 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
            if boy.velocity < -1:
                boy.velocity = -1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)
        print(boy.velocity)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                    3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                        -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
class DashState:

    @staticmethod
    def enter(boy, event):
        if event == START_DASH or event == START_DASH2:
            boy.velocity *= 2
            boy.dashtimer = 1000
        if event == RIGHT_DOWN:
            boy.velocity += 2
            if boy.velocity > 2:
                boy.velocity = 2
        elif event == LEFT_DOWN:
            boy.velocity -= 2
            if boy.velocity < -2:
                boy.velocity = -2
        elif event == RIGHT_UP:
            boy.velocity -= 2
        elif event == LEFT_UP:
            boy.velocity += 2
        boy.dir = boy.velocity
    @staticmethod
    def exit(boy, event):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.dashtimer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)
        print(boy.velocity)
        if boy.dashtimer == 0:
            boy.add_event(STOP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.velocity == 2:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

next_state_table = {
        IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                    RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                    SLEEP_TIMER: SleepState, START_DASH:IdleState,
                    START_DASH2: IdleState, STOP_DASH: IdleState,
                    STOP_DASH2: IdleState},
        RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                   LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                   START_DASH: DashState, START_DASH2: DashState,
                   STOP_DASH: RunState, STOP_DASH2: RunState},
        SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                     LEFT_UP: RunState, RIGHT_UP: RunState,
                     START_DASH: SleepState,START_DASH2: SleepState},
        DashState: {RIGHT_UP: DashState, LEFT_UP: DashState,
                   LEFT_DOWN: DashState, RIGHT_DOWN: DashState,
                    STOP_DASH: RunState,STOP_TIMER: RunState,
                    STOP_DASH2: RunState},      
}







class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.dashtimer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)



    def add_event(self, event):
        self.event_que.insert(0, event)


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

