import random
from pico2d import *
import game_world
import game_framework

MIN_MOVE_SPEED = 50  # 50 pps = 1.5 meter per sec
MAX_MOVE_SPEED = 200  # 200 pps = 6 meter per sec

speed = random.randint(MIN_MOVE_SPEED,MAX_MOVE_SPEED)

class Brick:
    image = None

    def __init__(self):
        if Brick.image is None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y = 800, 200

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        global speed
        self.x += speed * game_framework.frame_time
        if self.x < 0:
            speed = speed * -1
        if self.x > 1600:
            speed = speed * -1

    def stop(self):
        pass
