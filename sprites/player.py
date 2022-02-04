import pygame as pg
import os
from sprites.entity import *
from pygame import Vector2
    

class Player(AnimationEntity):
    def __init__(self, 
                 game, 
                 spritesheet: pg.Surface, 
                 spritedata: dict, 
                 name: str, 
                 pos: Vector2, 
                 stats: dict, 
                 hitbox: list, 
                 curr_direction: str = "down"):
        super().__init__(game, spritesheet, spritedata, name, pos, stats, hitbox, curr_direction)
    
    def update(self, actions, dt, collisions):
        return super().update(actions, dt, collisions)
    
    def attack(self):
        pass
    
    