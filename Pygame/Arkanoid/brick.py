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

#i love bricks
class Brick(pygame.sprite.Sprite):
    
    
    #constructor
    def __init__(self, brickColour):
        super().__init__()
        
        #colour is colour, and hits stores the number of hits needed to break the brick. 
        self.color = brickColour
        self.hits = 1
        self.images = []#
        
        #Yes this is ugly. I haven't done it like this elsewhere, but I'll come back to fix it when I have the chance. 
        if brickColour != "silver":
            self.images.append(pygame.image.load("Assets/Bricks/brick_" + str(brickColour) + ".png").convert())
        else:
            self.images.append(pygame.image.load("Assets/Bricks/brick_" + str(brickColour) + ".png").convert())
            self.hits = 3
            for i in range(10):
                self.images.append(pygame.image.load("Assets/Bricks/brick_" + str(brickColour) + "_" + str(i+1) + ".png"))
        self.index = 0
        
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        

   
    #this is called when a ball hits a brick. 
    def brickHit(self, score):
        #Basically, this list holds the colour and respective score value for each colour. the function first reads the colour's index, and then takes the score to be the value of the next index - which is exactly why its formatted as it is. 
        colorScore = ['silver',50,'white',60, 'orange', 60, 'cyan',70,'green',80, 'red',90, 'blue', 100, 'pink', 110, 'yellow', 120]
        self.hits -= 1
        if self.hits == 0:
            score = score + colorScore[colorScore.index(self.color) + 1]
            self.kill()
            return score
        return score
    