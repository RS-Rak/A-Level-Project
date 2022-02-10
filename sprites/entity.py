
import pygame as pg
from sprites.animation import Animation
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
                 curr_direction : str = "down"):
        super().__init__(game)
        
        self.animation = Animation(spritesheet, spritedata, pos, curr_direction)
        self.image = self.animation.image
        self.rect = self.animation.rect
        self.name = name
        self.current_direction = curr_direction
        
        self.stats = stats
        self.speed = int(self.stats["ENTITY-SPEED"])
        self.attack_speed = int(self.stats["ATTACK-SPEED"])
        self.hp = int(self.stats["HP"])
        self.velocity = Vector2(0,0)
        
        self.collision_rect = pg.Rect(0,0,self.rect.w/2, self.rect.h/2)
        self.collision_rect.midbottom = self.rect.midbottom
    
    def update(self, actions, dt, collisions):
        self.get_actions(actions, dt)
        self.move(dt, collisions)
        
        
    def get_actions(self, actions, dt):
        actions["move"] = actions["left"] or actions["right"] or actions["up"] or actions["down"]
        self.direction_x = actions["right"] - actions["left"]
        self.direction_y = actions["down"] - actions["up"]
        
        self.get_direction(actions)
        self.animation.get_actions(actions, dt, self.current_direction)
        
        self.image = self.animation.image
        self.rect = self.animation.rect
    
            
    def move(self, dt, collisions):
        new_rect = self.collision_rect.move(self.direction_x, self.direction_y)
        if new_rect.collidelist(collisions) == -1:
            self.velocity = Vector2(self.speed * dt * self.direction_x, self.speed * dt * self.direction_y)
            self.rect.center += self.velocity 
        self.collision_rect = pg.Rect(0,0,self.rect.w/2, self.rect.h/2)
        self.collision_rect.midbottom = self.rect.midbottom
    
    
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
    
    def check_hits(self, entity):
        if entity.attack_hitbox != None:
            if entity.attack_hitbox.collide_rect(self.hitbox):
                self.take_damage(entity)

    def take_damage(self, entity):
        self.hp -= entity.damage
        if self.hp < 0: 
            self.state = "dead" #note, put something in game_world to check when the player is dead. 
        for x in entity.weapon.effects:
            pass #ok the plan here is to add the effect stuff. i.e. making it so that we have poison effects and stuff for the swords
    
    
    
    
    
    
    
    
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
    
        
    