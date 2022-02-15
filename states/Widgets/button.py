import pygame as pg
import os
import time 
from Utility.text import Text
#very simple, very nice button code. buttons usually consist of a 
class Button():
    def __init__(self, game):
        self.game = game 
        self.clicked, self.hover = False, False
        self.hover_time = 0
        self.selected = False
    
    def checkCol(self, pos, actions):
        self.mouse_pos = ((pos[0] / self.game.RATIO_X), (pos[1]/self.game.RATIO_Y)) 
        self.hover = self.rect.collidepoint(self.mouse_pos)
        self.clicked = actions["attack"] and self.hover
        if self.hover:
            self.image = self.images[1]
            if self.hover_time == 0:
                self.hover_time = time.time()
        else:
            if not self.selected: self.image = self.images[0]
            self.hover_time = 0

class TextButton(Button):
    def __init__(self, game, pos, text, color1, color2, font = None, 
                 align = 'center', bg_color = None):
        super().__init__(game)
        if font == None: font = self.game.button_font
        self.default_image = Text(font, text, 999, color1, bg_colour=bg_color).image
        self.hover_image = Text(font, text, 999, color2, bg_colour=bg_color).image
        self.images = [self.default_image, self.hover_image]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        setattr(self.rect, align, pos)
        
class Tab(Button): #for multi choice 
    def __init__(self, pos, image, image_hover, game, path, align, imageclicked, name):
        super().__init__(game)
        self.name = name
        self.images = [
            pg.image.load(os.path.join(path, image)),
            pg.image.load(os.path.join(path, image_hover)),
            pg.image.load(os.path.join(path, imageclicked))   
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        setattr(self.rect, align, pos)

    def checkCol(self, pos, actions):
        super().checkCol(pos, actions)
        if self.clicked == True: self.selected = True
        if self.selected == True: self.image = self.images[2]

class ImageButton(Button): #this is for inventory slots, as i also need some metadata for these - 
                            #particularly what type of item is allowed in them I might add more features soon, but this'll do for now.
    def __init__(self, pos, image, image_hover, game, path, align ="center", metadata = None):
        super().__init__(game)
        self.images = [pg.image.load(os.path.join(path, image)), pg.image.load(os.path.join(path,image_hover))]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        setattr(self.rect, align, pos)
        self.metadata = metadata


  
    