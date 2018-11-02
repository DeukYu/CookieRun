import game_framework
import main_state
import game_world
import obstacles
import random
import time

from pico2d import *


class Stage:
    def __init__(self):
        self.image_Stage2_BackGround = load_image('resource/stage/Second_Background.png')
        self.image_Stage2_FrontGround = load_image('resource/stage/Second_Frontground.png')
        self.image_Stage2_BottomGround = load_image('resource/stage/Second_bottom.png')
        self.Bx1_1 = 400
        self.Bx1_2 = 1200
        self.Fx1_1 = 700
        self.Fx1_2 = 2100
        self.Bottomx1_1 = 400
        self.Bottomx1_2 = 1200
        self.timer = get_time()
        self.Creat_timer = get_time()
        self.ob_creat = False


    def draw(self):
        self.image_Stage2_BackGround.clip_draw(0, 0, 800, 500, self.Bx1_1, 250, 800, 500)
        self.image_Stage2_BackGround.clip_draw(0, 0, 800, 500, self.Bx1_2, 250, 800, 500)
        self.image_Stage2_FrontGround.clip_draw(0, 0, 1400, 500, self.Fx1_1, 250, 1400, 500)
        self.image_Stage2_FrontGround.clip_draw(0, 0, 1400, 500, self.Fx1_2, 250, 1400, 500)
        self.image_Stage2_BottomGround.clip_draw(0, 0, 800, 500, self.Bottomx1_1, 250, 800, 500)
        self.image_Stage2_BottomGround.clip_draw(0, 0, 800, 500, self.Bottomx1_2, 250, 800, 500)

    def show_obstacles(self):
        obstacle = obstacles.Obstacles(random.randint(0, 5))
        game_world.add_object(obstacle, 0)
        self.ob_creat = True

    def update(self):
        if self.Bx1_1 <= - 400:
            self.Bx1_1 = 1200

        if self.Bx1_2 <= - 400:
            self.Bx1_2 = 1200

        if self.Fx1_1 <= - 700:
            self.Fx1_1 = 2100

        if self.Fx1_2 <= - 700:
            self.Fx1_2 = 2100

        if self.Bottomx1_1 <= - 400:
            self.Bottomx1_1 = 1200

        if self.Bottomx1_2 <= - 400:
            self.Bottomx1_2 = 1200

        self.Bx1_1 -= 10 * game_framework.frame_time
        self.Bx1_2 -= 10 * game_framework.frame_time

        self.Fx1_1 -= 100 * game_framework.frame_time
        self.Fx1_2 -= 100 * game_framework.frame_time

        self.Bottomx1_1 -= 100 * game_framework.frame_time
        self.Bottomx1_2 -= 100 * game_framework.frame_time

        print((get_time() - self.timer) % 1)
        if (get_time() - self.timer) % 1 < 0.00001:
            if self.ob_creat == False:
                self.show_obstacles()
        if (get_time() - self.Creat_timer) % 10:
            self.ob_creat = False
