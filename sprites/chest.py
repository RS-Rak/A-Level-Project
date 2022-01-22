import pygame as pg
import os 
from sprites.entity import *
from Utility.util import *

class Chest(Entity):
    def __init__(self, game,x,y,inv_id): 
        Entity.__init__(self, game)
        self.image = pg.image.load(os.path.join(self.game.sprite_dir, "chest.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        try:
            self.data = load_data(os.path.join("assets","saved_data","chests","{}.json".format(inv_id)), False)
        except:
            print("Couldn't load chest data!")
            self.data = {}
        