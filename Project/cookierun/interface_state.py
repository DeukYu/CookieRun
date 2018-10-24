from pico2d import *

import game_framework
import main_state

name = "interface_state"

imageLobby = None
imageStartButton = None
imageCookieButton = None
imagePetButton = None
imageCookieSelection = None
imageShowCookie = None
imageShowPet = None
imagePetSelection = None


class Lobby:
    def __init__(self):
        self.image = load_image('interface_bg.png')

    def draw(self):
        self.image.draw(400, 250)


class StartButton:
    def __init__(self):
            self.image = load_image('start_button.png')
            self.motion = 0

    def draw(self):
            self.image.clip_draw(150 * self.motion, 0, 150, 50, 600, 40)


class CookieSelectButton:
    def __init__(self):
        self.image = load_image('cookie_select.png')
        self.motion = 0

    def draw(self):
        self.image.clip_draw(125 * self.motion, 0, 125, 50, 615, 120)


class CookieSelectWindow:
    def __init__(self):
        self.image = load_image('interface_cookieselect.png')
        self.OnOff = 0
        self.Exit = 0

    def draw(self):
        if Click == 2:
            self.image.draw(400, 250)

class PetSelectButton:
    def __init__(self):
        self.image = load_image('pet_select.png')
        self.motion = 0

    def draw(self):
        self.image.clip_draw(105 * self.motion, 0, 105, 50, 625, 200)


class PetSelectWindow:
    def __init__(self):
        self.image = load_image('interface_petselect.png')
        self.Exit = 0

    def draw(self):
        if Click == 1:
            self.image.draw(400, 250)


class ShowCookie:
    def __init__(self):
        self.image = load_image('interface_character.png')

    def draw(self):
            self.image.clip_draw(200 * CharChoice, 0, 200, 160, 150, 100)


class ShowPet:
    def __init__(self):
        self.image = load_image('interface_pet.png')

    def draw(self):
        self.image.clip_draw(80 * PetChoice, 0, 80, 80, 60, 100)


def enter():
    global imageLobby, imageStartButton, imageCookieButton, imagePetButton, imageCookieSelection, imageShowCookie
    global imagePetSelection, imageShowPet
    imageLobby = Lobby()
    imageStartButton = StartButton()
    imageCookieButton = CookieSelectButton()
    imagePetButton = PetSelectButton()
    imageCookieSelection = CookieSelectWindow()
    imageShowCookie = ShowCookie()
    imageShowPet = ShowPet()
    imagePetSelection = PetSelectWindow()


def exit():
    global imageLobby, imageStartButton, imageCookieButton, imagePetButton, imageCookieSelection, imageShowCookie
    global imagePetSelection, imageShowPet
    del imageLobby
    del imageStartButton
    del imageCookieButton
    del imagePetButton
    del imageCookieSelection
    del imageShowCookie
    del imageShowPet
    del imagePetSelection


def handle_events():
    global x, y, Click, CharChoice, PetChoice
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, 500 - event.y - 1
            if Click == 0: # Lobby
                if 600 - 75 <= x <= 600 + 75 and 40 - 25 <= y <= 40 + 25:
                    imageStartButton.motion = 1
                else:
                    imageStartButton.motion = 0
                if 625 - 55 <= x <= 625 + 55 and 200 - 25 <= y <= 200 + 25:
                    imagePetButton.motion = 1
                else:
                    imagePetButton.motion = 0
                if 615 - 60 <= x <= 615 + 60 and 120 - 25 <= y <= 120 + 25:
                    imageCookieButton.motion = 1
                else:
                    imageCookieButton.motion = 0
            elif Click == 1: # Pet
                if 600 - 25 <= x <= 600 - 5 and 350 - 25 <= y <= 350 - 5:
                    imagePetSelection.Exit = 1
                if 150 + 10 <= y <= 150 + 33:
                    if 200 + 15 <= x <= 200 + 90:
                        PetChoice = 0
                        imagePetSelection.Exit = 1
                    elif 200 + 113 <= x <= 200 + 188:
                        PetChoice = 1
                        imagePetSelection.Exit = 1
                    elif 200 + 211 <= x <= 200 + 286:
                        PetChoice = 2
                        imagePetSelection.Exit = 1
                    elif 200 + 310 <= x <= 200 + 385:
                        PetChoice = 3
                        imagePetSelection.Exit = 1
            elif Click == 2: # Cookie
                if 600 - 25 <= x <= 600 - 5 and 350 - 25 <= y <= 350 - 5:
                    imageCookieSelection.Exit = 1
                if 150 + 10 <= y <= 150 + 33:
                    if 200 + 15 <= x <= 200 + 90:
                        CharChoice = 0
                        imageCookieSelection.Exit = 1
                    elif 200 + 113 <= x <= 200 + 188:
                        CharChoice = 1
                        imageCookieSelection.Exit = 1
                    elif 200 + 211 <= x <= 200 + 286:
                        CharChoice = 2
                        imageCookieSelection.Exit = 1
                    elif 200 + 310 <= x <= 200 + 385:
                        CharChoice = 3
                        imageCookieSelection.Exit = 1
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if Click == 0:
                if imagePetButton.motion == 1:
                    Click = 1
                elif imageCookieButton.motion == 1:
                    Click = 2
                elif imageStartButton.motion == 1:
                    game_framework.change_state(main_state)
            elif Click == 1:
                if imagePetSelection.Exit == 1:
                    Click = 0
                    imagePetSelection.Exit = 0
            elif Click == 2:
                if imageCookieSelection.Exit == 1:
                    Click = 0
                    imageCookieSelection.Exit = 0


x, y = 0, 0

Click, CharChoice, PetChoice = 0, 0, 0


def draw():
    clear_canvas()
    imageLobby.draw()
    imageStartButton.draw()
    imageCookieButton.draw()
    imagePetButton.draw()
    imageShowCookie.draw()
    imageShowPet.draw()
    imageCookieSelection.draw()
    imagePetSelection.draw()
    update_canvas()


def update():
    pass





