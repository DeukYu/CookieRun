import random
import json
import os

from pico2d import *
import game_framework
import game_world
import pause_state

from cookie import Cookie
from stage import Stage
from pet import Pet
from obstacles import Obstacle

name = "MainState"

cookie = None
background = None
pet = None
game_timer = None
obstacle = None

def enter():
    global cookie, stage, pet, game_timer, obstacle
    cookie = Cookie()
    stage = Stage()
    pet = Pet()
    obstacle = Obstacle()
    game_timer = get_time()
    game_world.add_object(stage, 0)
    game_world.add_object(cookie, 1)
    game_world.add_object(pet, 2)
    game_world.add_object(obstacle, 3)


def exit():
    game_world.clear()


def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
          game_framework.change_state(pause_state)
       else:
           cookie.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





