#oh boy, enemy code
from math import gamma
import pygame
import time 

#Enemy class - we love enemies yes we do. 
class Enemy(pygame.sprite.Sprite):
    
    #constructor 
    def __init__(self, enemy, door):
        #door refers to the top door it spawns from - whether its the left or right one
        super().__init__()
        
        #Similar to most animated things in this game, I store the relative images in an array and just iterate through when necessary. 
        self.hp = 1
        self.images = []
        self.index = 0
        
        for i in range(25):
           self.images.append(pygame.image.load("Assets/Enemies/enemy_{}_{}.png".format(enemy, str(i+1)))) 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        
        #Spawns the enemy depending on which door it spawns at. 
        if door == 'left':
            self.rect.x = 122
        else:
            self.rect.x = 434
        self.rect.y = 160
        self.velocity = [1,2]
           
    def animate(self, loopControl):
        #Loopcontrol is a concept I run through in the readme file.
        #Anyways, this just runs through the image list periodically, starting from 0 when it hits 25. 
        x = self.rect.x
        y = self.rect.y
        loopControl += 1
        if loopControl%5 == 0:
            loopControl = 0
            self.index += 1
            if self.index == 25:
                self.index = 0
            self.image =  self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            
        return loopControl
    
    #movement
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    

            
        
        