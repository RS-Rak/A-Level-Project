import pygame as pg
import os
from sprites.entity import *
from pygame import Vector2
from datetime import datetime  
from copy import deepcopy

# note finish adding attacks, i need this to work properly. 
class Player(AnimationEntity):
    def __init__(self, 
                 game, 
                 spritesheet: pg.Surface, 
                 spritedata: dict, 
                 name: str, 
                 pos: Vector2, 
                 stats: dict,
                 equippedweapon,
                 curr_direction: str = "down"):
        super().__init__(game, spritesheet, spritedata, name, pos, stats, curr_direction)
        
        self._layer = 3
        self.attack_hitbox = None
        self.state = "alive"
        self.weapon = deepcopy(equippedweapon)
        self.damage = self.calc_damage()
        self.hitbox = self.rect.inflate(-1.2,-1.2)
        self.effects = {} #note, i could replace this with a simple list of effect - what it effects, by how much, the amount, etc. 

        
    def update(self, actions, dt, collisions):
        super().update(actions, dt, collisions)
        self.hitbox = self.rect.inflate(-1.2, -1.2)
       # self.attack()
        #self.check_hits()
        self.apply_effects()
            
    def attack(self):
        if self.animation.current_list == self.animation.animation_dict["attack"][self.current_direction] and self.animation.current_frame < 6:
            if self.weapon.type == "sword":
                self.attack_hitbox = self.weapon.hitbox[self.current_direction]
        else: 
            self.attack_hitbox = None

    def apply_effects(self):
        for x in self.effects:
            pass

        
    def calc_damage(self):
        damage = self.weapon.damage
        try:damage += (self.effects[self.weapon.type] - self.effects[self.weapon.type])
        except: 
            try: self.game.error_log.append(ConsoleOutput(f"Couldn't get damage values for weapon {self.weapon.name}, of type {self.weapon.type}."))
            except: pass 
            #note to self, start building console soon. first get attacks to work tho kekw.  
                 
        
  
    
    