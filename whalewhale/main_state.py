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
        self.image = load_image('back.png')
    def draw(self):
        self.image.draw(400,300)

class Whale:

    speed = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3]

    def __init__(self):
        self.x, self.y = 400, 300
        #self.frame = 0
        self.image_right = load_image('rfish.png')
        self.image_left = load_image('fish.png')
        self.state = 4 #stop
        self.dir = True
        self.level = 0
        self.distance = Whale.speed[self.level] * frame_time

    def update(self):
        #self.frame = (self.frame + 1) % 8
        if self.state == 0 and self.y < 580: #up
            self.y += self.distance
        elif self.state == 1 and self.y > 20: #down
            self.y -= self.distance
        elif self.state == 2 and self.x < 750: #right
            self.x += self.distance
        elif self.state == 3 and self.x > 50: #left
            self.x -= self.distance

    def draw(self):
        #self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.level == 0:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 1:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 2:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 3:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 4:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 5:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 6:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 7:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 8:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)
        elif self.level == 9:
            if self.dir == True:
                self.image_right.draw(self.x, self.y)
            else:
                self.image_left.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 70, self.y - 50, self.x + 70, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class YellowFish:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(0,600)
        self.frame = 0
        self.image_right = load_image('Ryellowfish.png')
        self.image_left = load_image('Lyellowfish.png')
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
        #self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.dir == 0:
            #self.image_right.draw(self.x, self.y)
            self.image_right.clip_draw(self.frame*65, 0, 65, 40, self.x, self.y)
        else:
            #self.image_left.draw(self.x, self.y)
            self.image_left.clip_draw(self.frame*65, 0, 65, 40, self.x, self.y)

    def get_bb(self):
        return self.x - 32, self.y - 20, self.x + 32, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class GoldFish:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(0,600)
        self.frame = 0
        self.image_right = load_image('Rgoldfish.png')
        self.image_left = load_image('Lgoldfish.png')
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
        return self.x - 40, self.y - 25, self.x + 40, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class GreenFish:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(0,600)
        self.frame = 0
        self.image_right = load_image('Rgreenfish.png')
        self.image_left = load_image('Lgreenfish.png')
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
            self.image_right.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        else:
            self.image_left.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 30, self.x + 50, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Tuna:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(0,600)
        self.frame = 0
        self.image_right = load_image('Rtuna.png')
        self.image_left = load_image('Ltuna.png')
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
            self.image_right.clip_draw(self.frame*130, 0, 130, 78, self.x, self.y)
        else:
            self.image_left.clip_draw(self.frame*130, 0, 130, 78, self.x, self.y)

    def get_bb(self):
        return self.x - 65, self.y - 30, self.x + 65, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



current_time = 0.0

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time



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
                whale.state = 0
            if event.key == SDLK_DOWN:
                whale.state = 1
            if event.key == SDLK_RIGHT:
                whale.state = 2
                whale.dir = True
            if event.key == SDLK_LEFT:
                whale.state = 3
                whale.dir = False
        elif event.type != SDL_KEYDOWN:
            whale.state = 4

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
    global current_time
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
    current_time = get_time()


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




