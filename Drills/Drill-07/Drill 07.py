from pico2d import *
import random

# Game object class here


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Boy:
    def init(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Grass:
    def init(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
        
class SmallBall:
    def init(self):
        self.x = random.randint(41, 759)
        self.y = 599
        self.fall = random.randint(10,40)
        self.image = load_image('ball21x21.png')
    def update(self):
        if self.y > 62:
            self.y -= self.fall
            if self.y < 62:
                self.y = 62
    def draw(self):
        self.image.draw(self.x,self.y)
        
class BigBall:
    def init(self):
        self.x = random.randint(41, 759)
        self.y = 599
        self.fall = random.randint(10,40)
        self.image = load_image('ball41x41.png')
    def update(self):
        if self.y > 70:
            self.y -= self.fall
            if self.y < 70:
                self.y = 70
    def draw(self):
        self.image.draw(self.x,self.y)
        
boy = Boy()
grass = Grass()
smallball = SmallBall()
bigball = BigBall()

team = [Boy() for i in range(11)]

smallballAmount = random.randint(1, 19)
bigballAmount = 20 - smallballAmount

smallballs = [SmallBall() for i in range(smallballAmount)]
bigballs = [BigBall() for i in range(bigballAmount)]

open_canvas()

running = True
for boy in team:
    boy.init()
for bigball in bigballs:
    bigball.init()
for smallball in smallballs:
    smallball.init()
    
grass.init()
while running:
    handle_events()
    for boy in team:
        boy.update()
    for bigball in bigballs:
        bigball.update()
    for smallball in smallballs:
        smallball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for bigball in bigballs:
        bigball.draw()
    for smallball in smallballs:
        smallball.draw()
    update_canvas()
    delay(0.05)
close_canvas()
