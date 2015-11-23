__author__ = 'WJY'
from pico2d import *

class Back:
    def __init__(self):
        self.image = load_image('Resources//back.png')
        self.life_image = load_image('Resources//life_back.png')
        self.life_bar_back_image = load_image('Resources//life_bar_back.png')
        self.mission_image = load_image('Resources//mission_back_o.png')
        self.level_image = load_image('Resources//level_back.png')

        self.bgm = load_music('Sound//under the sea.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def draw(self):
        self.image.draw(400,300)
        self.life_image.draw(155, 560)
        self.life_bar_back_image.draw(190, 560)
        self.mission_image.draw(485, 70)
        self.level_image.draw(120, 70)

