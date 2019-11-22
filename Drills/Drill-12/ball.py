import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1280-1), random.randint(0, 1024-1)
        self.HP = 50
        self.type = 'Ball'

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


class BigBall(Ball):
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1280-1), random.randint(0, 1024-1)
        self.HP = 100
        self.type = 'BigBall'

    def get_bb(self): return self.x - 20, self.y - 20, self.x + 20, self.y + 20
