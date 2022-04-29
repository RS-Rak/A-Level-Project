import pygame as pg
import os 
from sprites.entity import *
from Utility.util import *


class Chest(Entity):
    def __init__(self, game,x,y,inv_id, curr_map: str): 
        Entity.__init__(self, game)
        self._layer = 2
        self.image = pg.image.load(os.path.join(self.game.sprite_dir, "chest.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        try:
            self.data = load_data(os.path.join("assets","saved_data","chests","{}.json".format(inv_id)), False)
        except:
            # maybe create a seperate entity raise error function? and have all children of Entity use this function instead?
            self.game.error_log.append(ConsoleOutput(f"On creation of map {curr_map}, couldn't find chest data for chest at world co-ordinates: {str(self.rect.center)}."))
            self.data = {}
        