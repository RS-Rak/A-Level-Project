import pygame as pg
import os

class Entity(pg.sprite.Sprite): #base sprite class. 
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game

    def update(self, actions, delta_time, tiles):
        pass
    
    def animate(self, delta_time, direction_x, direction_y):
        pass
    
    def load_sprites(self):
        pass

