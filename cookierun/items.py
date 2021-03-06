from pico2d import *

import cookie
import game_framework
import game_world
import main_state
import random
import obstacles
import interface_state
import math


class Items:
    image = None
    Sound = None

    def __init__(self, select=0, Item_PosX=800):
        self.select = select
        self.x = Item_PosX
        self.frame = 0
        self.t = 0
        self.Sound_On_Off = False
        if self.select == 0: # 젤리
            self.image = load_image('resource/items/Jelly.png')
            self.y = random.randint(125, 450)
            self.Left_Right = 12
            self.Up_Down = 16

        elif self.select == 1: # 실버 코인
            self.image = load_image('resource/items/Silver_Coin.png')
            self.y = random.randint(125, 450)
            self.Left_Right = 16
            self.Up_Down = 16

        elif self.select == 2:
            self.image = load_image('resource/items/Gold_Coin.png')
            self.y = random.randint(125, 450)
            self.Left_Right = 16
            self.Up_Down = 16

        elif self.select == 3:
            self.image = load_image('resource/items/Power_Up.png')
            self.y = 250
            self.Left_Right = 25
            self.Up_Down = 25

        elif self.select == 4:
            self.image = load_image('resource/items/Hp_Up.png')
            self.y = 250
            self.Left_Right = 25
            self.Up_Down = 25

    def get_bb(self):
        return self.x - self.Left_Right, self.y - self.Up_Down, self.x + self.Left_Right, self.y + self.Up_Down

    def enter(self):
        pass

    def update(self):
        if main_state.stage.operation:
            self.x -= (250 * (main_state.cookie.pace + main_state.pet.speed)) * game_framework.frame_time

        if self.select == 1 or self.select == 2 or self.select == 3 or self.select == 4:
            self.frame = (self.frame + cookie.FRAMES_PER_ACTION4 * cookie.ACTION_PER_TIME1 * game_framework.frame_time) % 4

        if interface_state.CharChoice == 2 and math.sqrt((self.x - main_state.cookie.x) ** 2 + (self.y - main_state.cookie.y) ** 2) < 200:
            self.x = (1 - self.t) * self.x + self.t * main_state.cookie.x
            self.y = (1 - self.t) * self.y + self.t * main_state.cookie.y
            self.t += 0.1

        if self.x + self.Left_Right < 0:
            game_world.remove_object(self)

        elif main_state.collide(self, main_state.cookie):
            if self.select == 0:
                main_state.cookie.Eat_Jelly.play()
                if main_state.cookie.PowerUp:
                    main_state.cookie.jelly_cnt += 5
                else:
                    main_state.cookie.jelly_cnt += 1
            elif self.select == 1:
                main_state.cookie.Eat_Coin.play()
                if main_state.cookie.PowerUp:
                    main_state.cookie.coin_cnt += 5
                else:
                    main_state.cookie.coin_cnt += 1
            elif self.select == 2:
                main_state.cookie.Eat_Coin.play()
                if main_state.cookie.PowerUp:
                    main_state.cookie.coin_cnt += 10
                else:
                    main_state.cookie.coin_cnt += 2
            elif self.select == 3:
                main_state.cookie.Eat_Power.play()
                main_state.cookie.PowerUp = True
                main_state.cookie.pace += 0.3
                main_state.cookie.PowerUpTime = get_time()
            elif self.select == 4:
                main_state.cookie.Eat_Hp.play()
                main_state.cookie.CurHp += 30
                if main_state.cookie.CurHp > main_state.cookie.FullHp:
                    main_state.cookie.CurHp = main_state.cookie.FullHp
            game_world.remove_object(self)

    def draw(self):
        if self.select == 0: # 젤리
            self.image.clip_draw(self.frame * 0, 0, 24, 32, self.x, self.y, 24, 32)
            #draw_rectangle(*self.get_bb())
        elif self.select == 1 or self.select == 2:
            self.image.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x, self.y, 32, 32)
            #draw_rectangle(*self.get_bb())
        elif self.select == 3 or self.select == 4:
            self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y, 50, 50)
            #draw_rectangle(*self.get_bb())
