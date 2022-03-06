from Utility.util import *
import pygame as pg
from Utility.util import ConsoleOutput

class Animation():
    def __init__(self,
                 spritesheet: pg.Surface, 
                 spritedata: dict, 
                 pos,
                 curr_direction
                 ):
        self.spritesheet = spritesheet
        self.spritedata = load_data(spritedata)
        self.load_sprites()
        
        self.current_list = self.animation_dict["idle"][curr_direction]
        self.image = self.current_list[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
        self.looping = True
        self.idle = False
        self.animation_lock = False
    
    def get_actions(self, actions, dt, curr_direction):
        check = True #checks if currently idle
        for key in actions:
            if (key in self.spritedata) and actions[key]: #a key is being pressed so cannot be idle
                check = False
                if not self.animation_lock and self.current_list != self.animation_dict[key][curr_direction]:
                    self.set_list(key, curr_direction)            
                    break
        if check:    
            self.current_frame = 0
            self.current_list = self.animation_dict["idle"][curr_direction]
            self.idle = True
        
    def set_list(self, key, curr_direction):
        if (key in self.spritedata):
            self.current_list =  self.animation_dict[key][curr_direction]
            self.current_frame = 0
            self.current_fps = self.spritedata[key]["FPS"]
                        
            self.looping = self.spritedata[key]["LOOPING"]
            self.idle = False
            self.animation_lock = self.spritedata[key]["ANIMATION-LOCK"] 
        else: 
            ConsoleOutput(f"Error: {key} is not a valid animation for this entity.", (255,0,0))
        
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
           
        
    def load_sprites(self):
        self.animation_dict = {}
        self.current_frame, self.last_frame_update = 0,0
        self.current_list = None
        
        self.sprites = self.spritesheet.subsurface(self.spritedata["start"], self.spritedata["end"]) #if a shared spritesheet it grabs the relevant location. 
        for key in self.spritedata:
            if isinstance(self.spritedata[key], dict):
                self.load_sprites_list(key)
       
    
    def load_sprites_list(self, key):
        self.animation_dict.update({key: {}}) 
        for x in self.spritedata[key]:
            frames_list = []    
            if isinstance(self.spritedata[key][x], dict):       
                for frame in range(len(self.spritedata[key][x]["frames"])):
                    frames_list.append(self.sprites.subsurface(self.spritedata[key][x]["frames"][frame], self.spritedata[key][x]["divisor"]))
                self.animation_dict[key][x] = frames_list