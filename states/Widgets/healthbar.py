import pygame as pg
from pygame import Vector2

class HealthBar():
    def __init__(self, path,pos, hp, rectpos = (0,0), length = 200):
        self.image = pg.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rectpos = rectpos
        self.rect.topleft = pos 
        self.current_hp = hp
        self.prev_hp = hp
        self.max_hp = hp
        self.hp_bar_length = length
        self.hp
        
    def update(self, velocity):
        self.rect.topleft += Vector2(velocity)
        if self.prev_hp != self.hp:
                pass
        
    
    def render(self, display,  camera = None):
        if camera != None:
            self.rect = camera.apply_rect(self.rect)
        display.blit(self.image, self.rect)
    
    def draw_health_bar(self):
        trans_width = 0
        trans_color = (255,255,255) #the health bar has a dark-souls like transition when damage is taken - this represents this. 
        
        if self.current_hp < self.prev_hp: 
            pass
        