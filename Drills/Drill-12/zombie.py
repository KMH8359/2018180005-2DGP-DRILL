import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 4000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images is None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/" + name + " (%d)" % i + ".png") for i in
                                       range(1, 11)]

    def __init__(self):
        # positions for origin at top, left
        positions = [(43, 750), (1118, 750), (1050, 530), (575, 220), (235, 33), (575, 220),
                     (1050, 530), (1118, 750)]
        self.patrol_positions = []
        self.HP = 0
        self.attack = False
        self.font = load_font('ENCR10B.TTF', 16)
        for p in positions:
            self.patrol_positions.append((p[0], 1024-p[1])) # convert for origin at bottom, left
        self.patrol_order = 1
        self.target_x, self.target_y = None, None
        self.x, self.y = self.patrol_positions[0]

        self.load_images()
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0
        self.build_behavior_tree()

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi

        return BehaviorTree.SUCCESS

    def find_player(self):
        boy = main_state.get_boy()
        distance = (boy.x - self.x)**2 + (boy.y - self.y)**2
        # if distance < (PIXEL_PER_METER * 8)**2:
        self.dir = math.atan2(boy.y - self.y, boy.x - self.x)
        return BehaviorTree.SUCCESS
        # else:
          #  self.speed = 0
          #  return BehaviorTree.FAIL

    def find_ball(self):
        balls = main_state.get_balls()
        for ball in balls:
            distance = (ball.x - self.x)**2 + (ball.y - self.y)**2
            if ball:
                self.dir = math.atan2(ball.y - self.y, ball.x - self.x)
                return BehaviorTree.SUCCESS
            else:
                self.speed = 0
        return BehaviorTree.FAIL

    def move_to_player(self):
        boy = main_state.get_boy()
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS

    def run_from_player(self):
        boy = main_state.get_boy()
        if boy.HP > self.HP:
            self.speed = -RUN_SPEED_PPS
            self.dir = math.atan2(boy.y - self.y, boy.x - self.x)
            self.calculate_current_position()
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def move_to_ball(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS

    def attack_player(self):
        boy = main_state.get_boy()
        if main_state.collide(self, boy):
            self.attack = True
        else:
            self.attack = False
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        return BehaviorTree.SUCCESS

    def get_next_position(self):
        self.target_x, self.target_y = self.patrol_positions[self.patrol_order % len(self.patrol_positions)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS

    def move_to_target(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x)**2 + (self.target_y - self.y)**2

        if distance < PIXEL_PER_METER**2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        #wander_chase_node = SelectorNode("WanderChase")
        #wander_node = LeafNode("Wander", self.wander)
        chase_node = SelectorNode("Chase")

        about_ball_node = SequenceNode("Ball")
        find_ball_node = LeafNode("Find Ball", self.find_ball)
        move_to_ball_node = LeafNode("Move to Ball", self.move_to_ball)
        about_ball_node.add_children(find_ball_node, move_to_ball_node)

        about_player_node = SequenceNode("Player")
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        about_player_node.add_children(find_player_node, move_to_player_node)

        #move_node = SelectorNode("Move")
        #run_from_player_node = LeafNode("Run from Player", self.run_from_player)
        #move_to_attack_player_node = SequenceNode("Move and Attack")
        #attack_player_node = LeafNode("Attack", self.attack_player)
        #move_to_attack_player_node.add_children(move_to_player_node, attack_player_node)
        #move_node.add_children(run_from_player_node, move_to_attack_player_node )

        chase_node.add_children(about_ball_node, about_player_node)
       #wander_chase_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(chase_node)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.bt.run()

    def draw(self):
        self.font.draw(self.x - 50, self.y + 70, '(HP: %d)' % self.HP, (255, 255, 0))
        if math.cos(self.dir) < 0:
            if self.attack:
                Zombie.images['Attack'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                if self.speed == 0:
                    Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
                else:
                    Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.attack:
                Zombie.images['Attack'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                if self.speed == 0:
                    Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
                else:
                    Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)

    def handle_event(self, event):
        pass
