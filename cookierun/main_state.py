import random
import json
import os

from pico2d import *
import game_framework
import game_world

from cookie import Cookie
from background import Background
from pet import Pet

name = "MainState"

cookie = None
background = None
pet = None


def enter():
    global cookie, background, pet
    cookie = Cookie()
    background = Background()
    pet = Pet()
    game_world.add_object(background, 0)
    game_world.add_object(cookie, 1)
    game_world.add_object(pet, 0)


def exit():
    game_world.clear()


def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           game_framework.quit()
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





