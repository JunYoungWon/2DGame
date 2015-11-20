import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

move = True

whale = None
back = None
yellowfish = None
goldfish = None
greenfish = None
tuna = None
running = True

class Back:
    def __init__(self):
        self.image = load_image('Resources//back.png')
        self.life_image = load_image('Resources//life_back.png')
        self.life_bar_back_image = load_image('Resources//life_bar_back.png')
        self.life_bar_image = load_image('Resources//life_bar.png')
        self.mission_image = load_image('Resources//mission_back_o.png')
        self.level_image = load_image('Resources//level_back.png')
    def draw(self):
        self.image.draw(400,300)
        self.life_image.draw(155, 560)
        self.life_bar_back_image.draw(190, 560)
        self.life_bar_image.draw(190, 560)
        self.mission_image.draw(485, 70)
        self.level_image.draw(120, 70)


class Whale:

    PIXEL_PER_METER = (10.0 / 0.3)  #10 pixel 30cm
    RUN_SPEED_KMPH = 20.0   #km / hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 10.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    speed = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3]
    UP, DOWN, LEFT, RIGHT, STOP = 0, 1, 2, 3, 4

    image_right = None

    def __init__(self):
        self.x, self.y = 400, 300

        self.image_right = [load_image('Resources//1R.png'),
                            load_image('Resources//2R.png'),
                            load_image('Resources//3R.png'),
                            load_image('Resources//4R.png'),
                            load_image('Resources//5R.png'),
                            load_image('Resources//6R.png'),
                            load_image('Resources//7R.png'),
                            load_image('Resources//8R.png'),
                            load_image('Resources//9R.png'),
                            load_image('Resources//10R.png')]

        self.image_left = [load_image('Resources//1L.png'),
                            load_image('Resources//2L.png'),
                            load_image('Resources//3L.png'),
                            load_image('Resources//4L.png'),
                            load_image('Resources//5L.png'),
                            load_image('Resources//6L.png'),
                            load_image('Resources//7L.png'),
                            load_image('Resources//8L.png'),
                            load_image('Resources//9L.png'),
                            load_image('Resources//10L.png')]

        self.level = 0
        self.state = Whale.STOP
        self.dir = True


    def update(self):
        # distance = Whale.speed[self.level]
        if self.state == Whale.UP and self.y < 580: #up
            self.y += 2
        elif self.state == Whale.DOWN and self.y > 20: #down
            self.y -= 2
        elif self.state == Whale.RIGHT and self.x < 750: #right
            self.x += 2
        elif self.state == Whale.LEFT and self.x > 50: #left
            self.x -= 2

    def draw(self):
        if self.dir == True:
            self.image_right[self.level].draw(self.x, self.y)
        else:
            self.image_left[self.level].draw(self.x, self.y)

    def get_bb(self):
        if self.level == 0 or self.level == 1:
            return self.x - 13 *(self.level + 1), self.y - 13 * (self.level + 1),\
               self.x + 13 * (self.level + 1), self.y + 13 * (self.level + 1)

        else:
            return self.x - (self.level + 1) * 10, self.y - (self.level + 1) * 8,\
                   self.x + (self.level + 1) * 10, self.y + (self.level + 1) * 7


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class YellowFish:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(100,600)
        self.frame = 0
        self.image_right = load_image('Resources//Ryellowfish.png')
        self.image_left = load_image('Resources//Lyellowfish.png')
        self.speed = random.randint(3,5)

    def update(self):
        self.frame = (self.frame + 1) % 6
        if self.dir == 0:
            self.x += self.speed
        else:
            self.x -= self.speed

        if self.dir == 0 and self.x > 800:
            self.dir = 1
        elif self.dir == 1 and self.x < 0:
            self.dir = 0

    def draw(self):
        if self.dir == 0:
            self.image_right.clip_draw(self.frame*40, 0, 40, 25, self.x, self.y)
        else:
            self.image_left.clip_draw(self.frame*40, 0, 40, 25, self.x, self.y)

    def get_bb(self):
        return self.x - 18, self.y - 10, self.x + 18, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class GoldFish:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(100,600)
        self.frame = 0
        self.image_right = load_image('Resources//Rgoldfish.png')
        self.image_left = load_image('Resources//Lgoldfish.png')
        self.speed = random.randint(3,6)

    def update(self):
        self.frame = (self.frame + 1) % 6
        if self.dir == 0:
            self.x += self.speed
        else:
            self.x -= self.speed

        if self.dir == 0 and self.x > 800:
            self.dir = 1
        elif self.dir == 1 and self.x < 0:
            self.dir = 0

    def draw(self):
        if self.dir == 0:
            self.image_right.clip_draw(self.frame*80, 0, 80, 60, self.x, self.y)
        else:
            self.image_left.clip_draw(self.frame*80, 0, 80, 60, self.x, self.y)

    def get_bb(self):
        return self.x - 35, self.y - 12, self.x + 35, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class GreenFish:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(100,600)
        self.frame = 0
        self.image_right = load_image('Resources//Rgreenfish.png')
        self.image_left = load_image('Resources//Lgreenfish.png')
        self.speed = random.randint(2,5)

    def update(self):
        self.frame = (self.frame + 1) % 6
        if self.dir == 0:
            self.x += self.speed
        else:
            self.x -= self.speed

        if self.dir == 0 and self.x > 800:
            self.dir = 1
        elif self.dir == 1 and self.x < 0:
            self.dir = 0

    def draw(self):
        if self.dir == 0:
            self.image_right.clip_draw(self.frame*120, 0, 120, 120, self.x, self.y)
        else:
            self.image_left.clip_draw(self.frame*120, 0, 120, 120, self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 25, self.x + 40, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Tuna:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(100,600)
        self.frame = 0
        self.image_right = load_image('Resources//Rtuna.png')
        self.image_left = load_image('Resources//Ltuna.png')
        self.speed = random.randint(3,6)

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.dir == 0:
            self.x += self.speed
        else:
            self.x -= self.speed

        if self.dir == 0 and self.x > 800:
            self.dir = 1
        elif self.dir == 1 and self.x < 0:
            self.dir = 0

    def draw(self):
        if self.dir == 0:
            self.image_right.clip_draw(self.frame*175, 0, 175, 105, self.x, self.y)
        else:
            self.image_left.clip_draw(self.frame*175, 0, 175, 105, self.x, self.y)

    def get_bb(self):
        return self.x - 53, self.y - 25, self.x + 53, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())




def enter():
    global whale, back, yellowfish, goldfish, greenfish, tuna
    whale = Whale()
    back = Back()
    yellowfish = [YellowFish() for i in range(7)]
    goldfish = [GoldFish() for i in range(7)]
    greenfish = [GreenFish() for i in range(3)]
    tuna = [Tuna() for i in range(3)]

def exit():
    close_canvas()

def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
               running = False
               game_framework.change_state(title_state)
            if event.key == SDLK_UP:
                whale.state = Whale.UP
            if event.key == SDLK_DOWN:
                whale.state = Whale.DOWN
            if event.key == SDLK_RIGHT:
                whale.state = Whale.RIGHT
                whale.dir = True
            if event.key == SDLK_LEFT:
                whale.state = Whale.LEFT
                whale.dir = False
        elif event.type != SDL_KEYDOWN:
            whale.state = Whale.STOP

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def update():
    whale.update()
    for i in yellowfish:
        i.update()
        if collide(whale, i):
            yellowfish.remove(i)

    for i in goldfish:
        i.update()
        if collide(whale, i):
            goldfish.remove(i)

    for i in greenfish:
        i.update()
        # if collide(whale, i):
        #     greenfish.remove(i)

    for i in tuna:
        i.update()
        # if collide(whale, i):
        #     tuna.remove(i)


def draw():
    clear_canvas()
    back.draw()
    for i in yellowfish:
        i.draw()
        i.draw_bb()
    for i in goldfish:
        i.draw()
        i.draw_bb()
    for i in greenfish:
        i.draw()
        i.draw_bb()
    for i in tuna:
        i.draw()
        i.draw_bb()
    whale.draw()
    whale.draw_bb()

    update_canvas()
    delay(0.05)




