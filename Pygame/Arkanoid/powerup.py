import pygame, sys
from pygame.locals import *

#-Variables-------------#
#Colours
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARKBLUE = (0,0,55)


class Powerup(pygame.sprite.Sprite):
    def __init__(self, powerup):
        super().__init__()
        self.images =[]
        self.index = 0
        self.powerup = powerup
        for i in range(8):
            path = "Assets/MainMenu/powerup_{}_{}.png".format(self.powerup, str(i+1))
            self.images.append(pygame.image.load(path).convert_alpha())
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
    
    def animate(self, loopControl):
        loopControl += 1
        x = self.rect.x
        y = self.rect.y
        if loopControl%10 == 0:
            self.index = self.index + 1
            if self.index == 8:
                self.index = 0
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            loopControl = 0
        return loopControl
        
    def update(self):
        self.rect.y += 3
        
    