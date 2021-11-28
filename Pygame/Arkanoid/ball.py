import pygame, sys
from pygame.locals import *
from random import randint

#-Variables-------------#
#Colours
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARKBLUE = (0,0,55)


#This is my ball class
class Ball(pygame.sprite.Sprite):
    
    #constructor
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.image.load("Assets/Ball/ball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.baseVel = 4
        #When it spawns, we want it to initially not move so we can spawn in the player animation. 
        self.velocity = [0,0]
        
        
    def update(self):
        #Updates ball position. 
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def stuck(self, paddle, diff, caughtRN):
        #This is for the catch powerup. Diff is explained below. When the ball hits the paddle, it stops moving. 
        if paddle.powerup == 'catch' and caughtRN == True:
            self.rect.y = 750
            self.rect.x = paddle.rect.x + (paddle.rect.w)/2 + diff
        
    def paddleBounce(self, paddle, isCatch):
        #this is the difference from the center to one of the sides. diff is the difference from the paddle center to the current ball pos. Can be negative. 
        baseDiff = (paddle.rect.w)/2
        diff = (self.rect.x + 5) - (paddle.rect.x + paddle.rect.w/2)
    

        #this is slightly complex - what's its saying is that assuming the ball bounces on the right side of the paddle, its velocity is dependent on wheere it bounced - if it bounced in the center of the paddle, diff is very small, so x velocity is small and therefore it bounces almost straight up. The diff < 0 is just doing the same in the opposite direction. By adjusting the last value (1.2), I can change how violent these changes will be. 
        #also if catch powerup is active then it saves this velocity, so that it can apply it when the user releases the ball. 
        if isCatch:
            savedXVel = diff/baseDiff * self.baseVel * 1.2
            self.velocity[0] = 0 
            self.velocity[1] = 0 
            return savedXVel, True, True, diff
        else:
            self.velocity[0] = diff/baseDiff * self.baseVel * 1.2
        self.velocity[1] = -self.velocity[1]
     
    def bounce(self):
        #This is just a nice general bounce for bricks - it flips y velocity when it hits a brick. I wish I could make it more complex, but I just didn't have the time. 
            self.velocity[0] = self.velocity[0]
            self.velocity[1] = -self.velocity[1]
            
    def slow(self, multiplier): 
        #When this function is called, the ball is slowed by a specified amount. 
        self.velocity[0] = self.velocity[0] * multiplier
        self.velocity[1] = self.velocity[1] * multiplier
        
        
#add an if ball.rect.x and compare brick.rect.y to see if side collision. 