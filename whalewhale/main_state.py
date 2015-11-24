import random
import json
import os

from pico2d import *

import game_framework
import title_state
from main_state_back import Back

name = "MainState"

move = True

whale = None
back = None
yellowfish = None
goldfish = None
greenfish = None
tuna = None
shark = None
running = True

yellow_count = [3, 4, 5, 4, 4, 5, 3, 4, 4, 5]
gold_count = [0, 0, 0, 3, 4, 5, 3, 4, 4, 5]
green_count = [0, 0, 0, 0, 0, 0, 3, 3, 3, 5]
tuna_count = [0, 0, 0, 0, 0, 0, 0, 0, 3, 5]







class Whale:

    PIXEL_PER_METER = (10.0 / 0.1)  #10 pixel 30cm
    RUN_SPEED_KMPH = 1.0   #km / hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 10.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    UP, DOWN, LEFT, RIGHT, STOP = 0, 1, 2, 3, 4

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
        self.level_up_image = load_image('Resources//level_up.png')
        self.life_bar_image = load_image('Resources//life_bar.png')
        self.mission_count_image = [load_image('Resources//mission_count_1.png'),
                                    load_image('Resources//mission_count_2.png'),
                                    load_image('Resources//mission_count_3.png'),
                                    load_image('Resources//mission_count_4.png'),
                                    load_image('Resources//mission_count_5.png')]
        self.level_count_image = [load_image('Resources//level_count_1.png'),
                                  load_image('Resources//level_count_2.png'),
                                  load_image('Resources//level_count_3.png'),
                                  load_image('Resources//level_count_4.png'),
                                  load_image('Resources//level_count_5.png'),
                                  load_image('Resources//level_count_6.png'),
                                  load_image('Resources//level_count_7.png'),
                                  load_image('Resources//level_count_8.png'),
                                  load_image('Resources//level_count_9.png'),
                                  load_image('Resources//level_count_10.png')]

        self.level = 0
        self.state = Whale.STOP
        self.dir = True
        self.hp = 220
        self.distance = 0
        self.eat_yellow = yellow_count[self.level]
        self.eat_gold = gold_count[self.level]
        self.eat_green = green_count[self.level]
        self.eat_tuna = tuna_count[self.level]

        self.eat_sound = load_music('Sound//eat.mp3')
        self.eat_sound.set_volume(100)

        self.current_time = get_time()
        self.frame_time = get_time() + self.current_time


    def update(self):
        # self.distance = 20 * self.frame_time
        self.distance = self.RUN_SPEED_PPS * self.frame_time
        if self.state == Whale.UP and self.y < 580: #up
            self.y += self.distance
        elif self.state == Whale.DOWN and self.y > 20: #down
            self.y -= self.distance
        elif self.state == Whale.RIGHT and self.x < 750: #right
            self.x += self.distance
        elif self.state == Whale.LEFT and self.x > 50: #left
            self.x -= self.distance

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


    def level_up(self):
        self.level += 1
        self.eat_yellow = yellow_count[self.level]
        self.eat_gold = gold_count[self.level]
        self.eat_green = green_count[self.level]
        self.eat_tuna = tuna_count[self.level]

        if self.level >= 10:
            game_framework.change_state(title_state)

        self.level_ui()

    def level_ui(self):
        print("level up")
        self.level_up_image.draw(self.x - (self.level + 1) * 10 + 150, self.y - (self.level + 1) * 8 + 50)

    def ui_draw(self):
        self.life_bar_image.clip_draw(0, 0, self.hp, 30, self.hp/2 + 80, 560)

        if self.eat_yellow != 0:
            self.mission_count_image[self.eat_yellow-1].draw(250, 20)
        if self.eat_gold != 0:
            self.mission_count_image[self.eat_gold-1].draw(320, 20)
        if self.eat_green != 0:
            self.mission_count_image[self.eat_green-1].draw(416, 20)
        if self.eat_tuna != 0:
            self.mission_count_image[self.eat_tuna-1].draw(519, 20)

        self.level_count_image[self.level].draw(150,70)

    def eat(self):
        self.eat_sound.play()


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
            self.image_right.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        else:
            self.image_left.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

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
            self.image_right.clip_draw(self.frame*150, 0, 150, 90, self.x, self.y)
        else:
            self.image_left.clip_draw(self.frame*150, 0, 150, 90, self.x, self.y)

    def get_bb(self):
        return self.x - 53, self.y - 25, self.x + 53, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Shark:
    def __init__(self):
        self.dir = random.randint(0,1)
        self.x, self.y = 800 * self.dir, random.randint(100,600)
        self.image_right = load_image('Resources//Rshark.png')
        self.image_left = load_image('Resources//Lshark.png')

    def update(self):
        if self.dir == 0:
            self.x += 2
        else:
            self.x -= 2

        if self.dir == 0 and self.x > 800:
            self.dir = 1
        elif self.dir == 1 and self.x < 0:
            self.dir = 0

    def draw(self):
        if self.dir == 0:
            self.image_right.draw(self.x, self.y)
        else:
            self.image_left.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 140, self.y - 35, self.x + 140, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


def enter():
    global whale, back, yellowfish, goldfish, greenfish, tuna, shark

    whale = Whale()
    back = Back()

    yellowfish = [YellowFish() for i in range(20)]
    goldfish = [GoldFish() for i in range(7)]
    greenfish = [GreenFish() for i in range(7)]
    tuna = [Tuna() for i in range(7)]
    shark = [Shark() for i in range(3)]



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
            if event.key == SDLK_SPACE:
                whale.level_up()
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
    # current_time = get_time()
    whale.frame_time = get_time() - whale.current_time
    whale.current_time += whale.frame_time
    whale.update()

    if whale.eat_yellow == 0 and whale.eat_gold == 0 and whale.eat_green == 0 and whale.eat_tuna == 0:
            whale.level_up()

    if whale.hp <= 0:
        game_framework.change_state(title_state)

    if whale.level >= 0:
        for i in yellowfish:
            i.update()
            if collide(whale, i):
                yellowfish.remove(i)
                # whale.eat()
                if whale.eat_yellow > 0:
                    whale.eat_yellow -= 1
                if whale.hp < 220:
                    whale.hp += 1

    if whale.level >= 1:
        for i in goldfish:
            i.update()
            if collide(whale, i):
                if whale.level >= 3:
                    goldfish.remove(i)
                    # whale.eat()
                    if whale.eat_gold > 0:
                        whale.eat_gold -= 1
                    if whale.hp < 220:
                        whale.hp += 2
                else:
                    whale.hp -= 3

    if whale.level >= 3:
        for i in greenfish:
            i.update()
            if collide(whale, i):
                if whale.level >= 6:
                    greenfish.remove(i)
                    # whale.eat()
                    if whale.eat_green > 0:
                        whale.eat_green -= 1
                    if whale.hp < 220:
                        whale.hp += 2
                else:
                    whale.hp -= 4


    if whale.level >= 6:
        for i in tuna:
            i.update()
            if collide(whale, i):
                if whale.level >= 8:
                    tuna.remove(i)
                    # whale.eat()
                    if whale.eat_tuna > 0:
                        whale.eat_tuna -= 1
                    if whale.hp < 220:
                        whale.hp += 3
                else:
                    whale.hp -= 5

    if whale.level >= 8:
        for i in shark:
            i.update()
            if collide(whale, i):
                game_framework.change_state('title_state')






def draw():
    clear_canvas()
    back.draw()
    whale.ui_draw()

    if whale.level >= 0:
        for i in yellowfish:
            i.draw()
            i.draw_bb()

    if whale.level >= 1:
        for i in goldfish:
            i.draw()
            i.draw_bb()

    if whale.level >= 3:
        for i in greenfish:
            i.draw()
            i.draw_bb()

    if whale.level >= 6:
        for i in tuna:
            i.draw()
            i.draw_bb()

    if whale.level >= 8:
        for i in shark:
            i.draw()
            i.draw_bb()

    whale.draw()
    whale.draw_bb()

    update_canvas()
    delay(0.05)




