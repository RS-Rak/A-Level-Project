import pygame, sys
from pygame.locals import *
from menu import mainMenu, endMenu
from paddle import Paddle, Bullet
from ball import Ball
from brick import Brick
from powerup import Powerup
import time
from baseround import round 
from enemy import Enemy
# Setup pygame/window ------------------------------------#
mainClock = pygame.time.Clock()
pygame.init()
flags = DOUBLEBUF
pygame.font.init()
windowSize = (600,800)
screen = pygame.display.set_mode(windowSize, 0, 32)
pygame.display.set_caption("Arkanoid")

#-Variables-------------#
#Colours
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARKGREEN =(0,100,0)
YELLOW = (255, 255, 0)
running =  True
roundstart = True
onMenu = True
roundnumber = 1
maxrounds = 4
#Font paths
optimusFont = 'Assets/Fonts/optimus.ttf'
generationFont = 'Assets/Fonts/generation.ttf'
scoreFile = "Assets/textfiles/highscore.txt"


#This is my write function, it creates a text image to be blitted onto the screen. 
def write(text, color, size, fontPath):
        font = pygame.font.Font(fontPath, size)
        text = font.render(text, 1, pygame.Color(color))
        return text
    

    
        
while running:
    #Runs main menu
    if onMenu:
        mainMenu(screen, mainClock, write)
        onMenu = False
    
    #Keeps running the rounds untill you fail. 
    gameOver, score, highscore = round(screen, mainClock, roundnumber, write, Brick, Paddle, Ball, Powerup, Bullet, Enemy)
    if gameOver == True:
        score += 1000 * roundnumber
        if score > int(highscore):
            #If you've set a new highscore, it writes it to the highscore text file. 
          with open(scoreFile, 'r+') as f:
              f.truncate(0)
              f.seek(0)
              f.write(str(score))
              f.close()
          highscore = score  
        #If you've lost, then it displays your score and highscore.
        endMenu(screen, mainClock, write, score, highscore)
        running = False
    else:
        #If you haven't lost, it just goes to the next round - up untill whatever is defined as the last programmed round. 
        roundnumber += 1
        if roundnumber >= maxrounds + 1:
            gameOver = True
            