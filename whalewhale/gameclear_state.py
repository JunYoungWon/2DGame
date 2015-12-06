import game_framework
import title_state
from pico2d import *


name = "GameclearState"
image = None
bgm =None


def enter():
    global  image
    image = load_image('Resources//game_clear.png')

    bgm = load_wav('Sound//game_over.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)



def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass






