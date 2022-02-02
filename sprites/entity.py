
import pygame as pg
import os
from pygame import Vector2
from Utility.util import *

class Entity(pg.sprite.Sprite): #base sprite class. 
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game

    def update(self, actions, delta_time, tiles):
        pass
    
    def load_sprites(self):
        pass




class AnimationEntity(Entity):
    def __init__(self, 
                 game, 
                 spritesheet: pg.Surface, 
                 spritedata: dict, 
                 name: str, 
                 pos: Vector2, 
                 stats: dict, 
                 hitbox: list, 
                 curr_direction : str = "right"):
        super().__init__(game)
        
        self.spritesheet = spritesheet
        self.spritedata = load_data(spritedata)
        self.name = name
        self.current_direction = curr_direction
        
        self.stats = stats
        self.speed = int(self.stats["entity-speed"])
        self.attack_speed = int(self.stats["attack-speed"])
        self.hp = int(self.stats["HP"])
        self.animation_lock = False #when you're in certain attacks you can't do others
        self.looping = True
        self.idle = False
        
        self.load_sprites()
        self.current_list = self.animation_dict["move"][self.current_direction]
        self.image = self.current_list[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.hitbox_data = hitbox
        self.hitbox = pg.Rect(Vector2(self.rect.center) - Vector2(self.hitbox_data[0]), Vector2(self.rect.center) + Vector2(self.hitbox[1]))
        self.collision_rect = pg.Rect(0,0,self.rect.w/2, self.rect.h/2)
        self.collision_rect.midbottom = self.rect.midbottom
    
    def update(self, actions, dt, collisions):
        self.get_actions(actions, dt)
        self.move(dt, collisions)
        
        
    def get_actions(self, actions, dt):
        actions["move"] = actions["left"] or actions["right"] or actions["up"] or actions["down"]
        self.direction_x = actions["right"] - actions["left"]
        self.direction_y = actions["down"] - actions["up"]
        self.get_direction()
        
        if actions["attack"] and not self.animation_lock:
            self.current_list = self.animation_dict["attack"][self.current_direction]
            self.current_frame = 0
            self.current_fps = self.attack_speed
            self.looping, self.idle = False, False
            self.animation_lock = True
            
        if actions["move"] and not self.animation_lock:
            self.get_direction()
            self.current_list = self.animation_dict["move"][self.current_direction]
            self.current_fps = 8
            self.looping = True
            self.idle = False
        else:
            self.current_frame = 0
            self.current_list = self.animation_dict["move"][self.current_direction]
            self.idle = True
        self.animate(dt)
        
        
    def animate(self, delta_time):
        if not self.idle:
            self.last_frame_update += delta_time
            if self.last_frame_update > 1/self.current_fps:
                self.last_frame_update = 0
                self.current_frame += 1
                if self.current_frame >= len(self.current_list):
                    if self.looping: 
                        self.current_frame = 0
                    else: 
                        self.current_frame = 0 
                        self.current_list = None
                        self.animation_lock = False
        self.image = self.current_list[self.current_frame]
        pos = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = pos
            
    def move(self, dt, collisions):
        new_rect = self.collision_rect.move(self.direction_x, self.direction_y)
        if new_rect.collidelist(collisions) == -1:
            self.rect.x += round(self.speed * dt * self.direction_x)
            self.rect.y += round(self.speed * dt * self.direction_y) 
        self.hitbox = pg.Rect(Vector2(self.rect.center) - Vector2(self.hitbox_data[0]), Vector2(self.rect.center) + Vector2(self.hitbox[1]))
        self.collision_rect = pg.Rect(0,0,self.rect.w/2, self.rect.h/2)
        self.collision_rect.midbottom = self.rect.midbottom
    
    
    
    def load_sprites(self):
        self.animation_dict = {}
        self.current_frame, self.last_frame_update = 0,0
        self.current_list = None
        
        self.sprites = self.spritesheet.subsurface(self.spritedata["start"], self.spritedata["end"]) #if a shared spritesheet it grabs the relevant location. 
        
        try: self.load_sprite_list("move") 
        except KeyError: print("no move sprites!") 
        try: self.load_sprite_list("attack")
        except KeyError: print("no attack sprites!")
    
    def load_sprite_list(self, key):
        self.animation_dict.update({key: {}}) 
        for x in self.spritedata[key]:
            frames_list = []           
            for frame in range(len(self.spritedata[key][x]["frames"])):
                frames_list.append(self.sprites.subsurface(self.spritedata[key][x]["frames"][frame], self.spritedata[key][x]["divisor"]))
            self.animation_dict[key][x] = frames_list
    
    def entity_in_sight(self, entity1, entity2, walls): # player rect
        entity1_pos = Vector2(entity1.center)
        entity2_pos = Vector2(entity2.center)
        for i in range(walls):
            if i.rect.clipline(entity1_pos, entity2_pos):
                return False
        if (abs(entity1_pos - entity2_pos)).magnitude() > entity2.sight_range: #if the player is outside of the sight range of the entity it does nothing. 
            return False
        else:
            return True

    def get_direction(self, actions):
        if actions["left"]:
            self.current_direction = "left"
        if actions["right"]:
            self.current_direction = "right"
        if actions["up"]:
            self.current_direction = "up"
        if actions["down"]:
            self.current_direction = "down"
    
    
    
    
    
class Enemy(AnimationEntity):
    def __init__(self, 
                 game, 
                 spritesheet: pg.Surface, 
                 spritedata: dict, 
                 name: str, 
                 pos: Vector2, 
                 stats: dict, 
                 hitbox: list, 
                 path,
                 hostile : bool,
                 curr_direction : str = "right"):
        
        super().__init__(game, spritesheet, spritedata, name, pos, stats, hitbox, curr_direction)
        self.actions = {
            "move": False, "left": False, "right": False, "up": False, "down": False, "attack": False, "alt-attack":False
        } #this is the action dict for the AI
        self.modes = { #These are the AI "modes", and determine what actions it takes.
            "idle": False, 
            "set-path": False,
            "wandering": False,
            "attacking": False
        }
        self.hostility = hostile #if it's hostile we need this to check 
        self.path = path
        self.name = name
   
         
    def move():
        pass
    
            
    def make_decision(self, player, walls, entity): #this function allows the AI to choose what action to take next
        if self.state == "idle" and not self.hostility: #if it's not hostile AND idle it doesn't move. 
            return Vector2(0,0) 
        elif self.modes["idle"] and self.hostility:
             if self.entity_in_sight(player, entity, walls):
                 self.modes["idle"] = False
                 self.modes["attacking"] =  True
    
        
    