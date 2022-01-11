import pygame as pg
import os
from sprites.entity import *
from pygame import Vector2

class Player(Entity):
    def __init__(self,x,y, game):
        Entity.__init__(self,game)
        self.load_sprites()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_direction = 0   #what this and the dict below are for is for when i need to use the current direction of the entity
        self.current_direction_dict ={
            "front": Vector2(self.rect.h, 0),
            "back": 0,
            "left": 0,
            "right":0
            #they're all 0 for now because I haven't got around to it yet 
        }
        
    def update(self, actions, delta_time, tiles):
        #get the direction from inputs - i'm subtracting them since true has a value of 1 while false has 0, so if both keys are being hit it doesnt. 
        direction_x = actions['right'] - actions["left"]
        direction_y = actions['down'] - actions["up"]
        #animating the sprite
        self.animate(delta_time, direction_x, direction_y)
        if self.check_player_col(tiles,direction_x, direction_y):
            pass
        else:
            old_x = self.rect.x 
            old_y = self.rect.y
            self.rect.x += round(100 * delta_time * direction_x)
            self.rect.y += round(100 * delta_time * direction_y)
            #self.check_if_stuck(tiles, old_x, old_y)
    
                  
    def check_if_stuck(self, tiles, old_x, old_y):
        if self.rect.collidelistall(tiles):
            self.rect.x = old_x
            self.rect.y = old_y
    
    def check_col(self, list): #note, i can just combine this into the player_check_col list? 
        check = False  
        index = None
        collision_rect = pg.Rect((self.rect.midleft),(self.rect.w, self.rect.h/2) )
        for i in range(len(list)):
            if pg.Rect.colliderect(collision_rect, list[i]):
                check = True
                index = i
        return check, index
    
       
    def animate(self, delta_time, direction_x, direction_y):
        #checks how long since last frame
        self.last_frame_update += delta_time
        if not (direction_x or direction_y):#if no direction pressed, set image to idle. 
            self.image = self.curr_animation_list[0]
            return 
        # If an image was pressed, use the appropriate list of frames
        
        if direction_x:
            if direction_x > 0: 
                self.curr_animation_list = self.right_sprites
                self.current_direction = "right"
            if direction_x < 0: 
                self.curr_animation_list = self.left_sprites
                self.current_direction = "left"
        if direction_y:
            if direction_y > 0: 
                self.curr_animation_list = self.front_sprites
                self.current_direction = "front"
            if direction_y < 0: 
                self.curr_animation_list = self.back_sprites
                self.current_direction = "back"
        #advance the animation if enough time has passed.
        if self.last_frame_update > .15:
            self.last_frame_update = 0
            self.current_frame = (self.current_frame + 1) % len(self.curr_animation_list)
        x = self.rect.x
        y = self.rect.y
        self.image = self.curr_animation_list[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
            
        
        
    def load_sprites(self):
        #loads in the frames for each direction
        self.front_sprites, self.back_sprites, self.left_sprites, self.right_sprites = [],[],[],[]
        self.player_dir = os.path.join(self.game.sprite_dir, "player")
        for i in range(1,5):
            self.front_sprites.append(pg.image.load(os.path.join(self.player_dir, "player_front{}.png".format(str(i)))).convert_alpha())
            self.back_sprites.append(pg.image.load(os.path.join(self.player_dir, "player_back{}.png".format(str(i)))).convert_alpha())
            self.left_sprites.append(pg.image.load(os.path.join(self.player_dir, "player_left{}.png".format(str(i)))).convert_alpha())
            self.right_sprites.append(pg.image.load(os.path.join(self.player_dir, "player_right{}.png".format(str(i)))).convert_alpha())
        #set it to be facing the front by default
        self.image = self.front_sprites[0]
        self.curr_animation_list = self.front_sprites
        #sets the current frame and last frame update to be
        self.current_frame, self.last_frame_update = 0,0
        
        
        
    def check_player_col(self, tiles, movement_x, movement_y):
        #new_rect = self.rect.move(movement_x, movement_y) 
        self.collision_rect = pg.Rect(0,0,self.rect.w/2, self.rect.h/2)
        self.collision_rect.midbottom = self.rect.midbottom 
        new_rect = self.collision_rect.move(movement_x, movement_y) 
        check = False
        if (new_rect.collidelist(tiles) != -1): #this tests every tile with the player rectangle
            check = True
        return check