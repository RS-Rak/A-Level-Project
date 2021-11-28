import pygame, sys
from pygame.locals import *
import time

#-Variables-------------#
#Colours
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARKBLUE = (0,0,55)

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        #I'm going to comment this part just so I can look back on it later. The images list is because there are so many damn animations for this paddle, so this will store all of them. self.index holds the current index of whichever image I'm actually using for the sprite. 
        path = "Assets/Paddle/"
        self.images = []
        self.index = 0
        self.images.append(pygame.image.load(path + "paddle.png"))
        self.powerup = ''
        
        #The second to ninth indexes will hold the death animation  
        for i in range(8):
            self.images.append(pygame.image.load(path + "paddle_explode_" + str(i+1) + ".png").convert_alpha())
        #The tenth to twenty-fifth indexes hold the laser transformation - very cool. 
        for i in range(16):
            self.images.append(pygame.image.load(path + "paddle_laser_" + str(i + 1) + ".png").convert_alpha())
        #The twenty-sixth to fourtieth indexes hold the initial spawn animation.
        for i in range(15):
            self.images.append(pygame.image.load(path + "paddle_materialize_" + str(i+1) + ".png").convert_alpha())
        #And finally, the fourtyfirst to fourtyninth index is w i d e  boy
        for i in range(9):
            self.images.append(pygame.image.load(path + "paddle_wide_" + str(i+1) + ".png").convert_alpha())
            
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        
    def animate(self, animation, spritelist, clock, screen, roundColor, topedge, leftedge, rightedge, lives, printlives):
        #that's a lot of parameters
        
        #So, first it needs to save the current x and y co-ords, so that we can put the new image back exactly where the old was. 
        x = self.rect.x
        y = self.rect.y
        
        #See readme for an explanation of loop control.
        loopControl = 0 
        #Similar to my trick in brick.py, each index is meant to be part of a group of 3 - one index holds the powerup name, and the other 2 hold the start and end index. 
        aniList = ['death',1,9,'laser',10,25,'expand',41,49,'spawn',26,40]
        self.index = aniList[aniList.index(animation) + 1]
        maxIndex = aniList[aniList.index(animation) + 2]
        
        while True:
            pygame.draw.rect(screen, roundColor, [0,150,600,800])
            screen.blit(leftedge, (0,150))
            screen.blit(rightedge, (578,150))
            screen.blit(topedge, (22,150))
            printlives(lives)
            self.image = self.images[self.index]
            if loopControl%6 == 0:
                self.index += 1
                if self.index == maxIndex:
                    if animation == 'spawn':
                        self.index = 0
                        self.image = self.images[self.index]
                    else:
                        self.index = maxIndex
                    self.rect = self.image.get_rect()
                    self.rect.x = x
                    self.rect.y = y
                    spritelist.draw(screen)
                    return
            loopControl += 1
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            spritelist.draw(screen)
            
            pygame.display.flip()
            clock.tick(60)
          

    def reset(self):
        x = self.rect.x
        y = self.rect.y
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.powerup = ''
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
	    #Check that you are not going too far (off the screen)
        if self.rect.x < 22:
          self.rect.x = 22
 
    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x + self.rect.w > 578:
          self.rect.x = 578 - self.rect.w
    
    def collectPowerup(self, powerup, spritelist, clock, screen, ball, roundColour, top, left, right, lives, printlives):
        #First runs the reset function to ensure the current powerup is cleared.
        self.reset()
        #Sets powerup
        self.powerup = powerup
        if self.powerup == 'laser' or self.powerup == 'expand':
            #These are the only 2 powerups which need animation.
            self.animate(powerup, spritelist, clock, screen, roundColour, top, left, right, lives, printlives)
        if self.powerup == 'slow':
            #see ball.py for a little more info on this. 
            ball.slow(0.75)
        #grabs the current time so it can limit the powerup to 20 seconds in baseround.py 
        start = time.time()
        return start
    
    
    


#this is the bullet for the laser powerup
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, paddle):
        super().__init__()
        self.group = pygame.sprite.Group()
        
        YELLOW = (255, 255, 0)
        
        self.image = pygame.Surface([5, 10])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, YELLOW, [0,0, 5, 10])
        self.rect = self.image.get_rect()
        self.rect.y = 750 
        if position == 'right':
            self.rect.x = paddle.rect.x + 50
        else:
            self.rect.x = paddle.rect.x + 25
            
    def update(self):
        self.rect.y -= 10
    
    def collision(self, bulletlist):
        
        self.kill()
        if bulletlist.index(self)%2 == 0:
            bulletlist[bulletlist.index(self) + 1].kill()
            bulletlist.pop(bulletlist.index(self) + 1)
        else:
            bulletlist[bulletlist.index(self) - 1].kill()
            bulletlist.pop(bulletlist.index(self) - 1)
        bulletlist.pop(bulletlist.index(self))
        return bulletlist