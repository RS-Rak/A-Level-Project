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
                 equippedweapon,
                 curr_direction: str = "down"):
        super().__init__(game, spritesheet, spritedata, name, pos, stats, hitbox, curr_direction)
        self.attack_hitbox = None
        self.state = "alive"
        self.weapon = equippedweapon
        self.damage = self.calc_damage()
        
        self.effects = {} #note, i could replace this with a simple list of effect - what it effects, by how much, the amount, etc. 

        
    def update(self, actions, dt, collisions):
        super().update(actions, dt, collisions)
        self.attack()
        self.check_hits()
        self.apply_effects()
            
    def attack(self):
        if self.animation.current_list == self.animation.animation_dict["attack"][self.current_direction]:
            if self.weapon.type == "sword":
                self.weapon.hitbox[self.current_direction] = self.attack_hitbox
        else: self.attack_hitbox = None

    def apply_effects(self):
        pass

        
    def calc_damage(self):
        damage = self.weapon
        try:damage += (self.effects[self.weapon.type] - self.effects[self.weapon.type])
        except: print(f"Couldn't get damage values for weapon {self.weapon.name}, of type {self.weapon.type}.")      
        
  
    
    