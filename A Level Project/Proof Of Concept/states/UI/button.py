import pygame as pg
import os

class Button():
    def __init__(self, x, y, image, image_hover, game, dir):
        self.game = game 
        self.image_unclicked = pg.image.load(os.path.join(game.button_dir, dir, image)).convert_alpha()
        self.image_hover = pg.image.load(os.path.join(game.button_dir, dir, image_hover ))
        self.images = [self.image_unclicked, self.image_hover]
        self.image = self.images[0] 
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked, self.hover = False, False
    
    def checkCol(self, pos, actions, game):
        self.mouse_pos = ((pos[0] / self.game.RATIO_X), (pos[1]/self.game.RATIO_Y)) 
        if self.rect.collidepoint(self.mouse_pos):
            #print("it has collided") #this is for debugging 
            if actions['attack']:
                self.clicked = True
            else:
                self.clicked = False
            self.hover = True
            self.image = self.images[1] # if its hovering, it shows a different img
        else:
            self.hover, self.clicked = False, False
            self.image = self.images[0]
    
    