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
        self.attack()
        #self.check_hits()
        self.apply_effects()
            
    def attack(self):
        if  self.animation.current_key == "attack" and self.animation.current_frame < 6:
            self.create_hitbox()
            if self.weapon.type == "sword":
                self.attack_hitbox = self.weapon.hitbox[self.current_direction]
        else: 
            self.attack_hitbox = None

    def create_hitbox(self):
        if self.weapon.type == "Melee":
                self.attack_hitbox = pg.Rect(self.weapon.hitbox)
                if self.current_direction == "left":
                    self.attack_hitbox.midright = self.rect.midleft
                elif self.current_direction == "right":
                    self.attack_hitbox.midleft = self.rect.midright
                elif self.current_direction == "up":
                    self.attack_hitbox.midbottom = self.rect.midtop
                elif self.current_direction == "down":
                    self.attack_hitbox.midtop = self.rect.midbottom
                self.raise_error(f"Successfully created a weapon hitbox, for weapon name {self.weapon.name} for Player character.")
    
    def apply_effects(self):
        for x in self.effects:
            pass

        
    def calc_damage(self):
        damage = self.weapon.damage
        try:damage += (self.effects[self.weapon.type] - self.effects[self.weapon.type])
        except: 
            try: self.raise_error(f"Couldn't get damage values for weapon {self.weapon.name}, of type {self.weapon.type}.")
            except: pass 
            #note to self, start building console soon. first get attacks to work tho kekw.  
                 
        
  
    
    