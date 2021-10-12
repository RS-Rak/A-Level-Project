import pygame, sys
from pygame.locals import *

pygame.init()
#Initialises pygame. 

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SKYBLUE = (3,207,252)
GRASS = (12,150,8)
BROWN = (130,63,34)
ROOF = (173, 144, 132)
YELLOW = (235, 231, 23)
DOOR = (23, 235, 210)
#OOOOH COLOURS

FPS = 60 #frames per second setting 
clock = pygame.time.Clock()

screenWidth = 1000
screenHeight = 1000
# screen height and width in pixels, its like this for pure convenience. 

screen = pygame.display.set_mode((screenWidth,screenHeight))
# Makes a display window the size of my monitor. 

anotherScreen = screen.convert_alpha()
#This gives another surface - one that allows us to create a partly transparent 

pygame.display.set_caption("My House")
x=800
done = False
while not done: #This is the main game loop - where all the magic happens babbyyyy
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    screen.fill(SKYBLUE)
    #Fills screen with my colour of choice

    pygame.draw.rect(screen, GRASS, [0,700,1000,300])
    #The grass

    pygame.draw.rect(screen, BROWN, [250,400,500,500])
    #The house
    
    pygame.draw.rect(screen, DOOR, [450,650,100,250] )
    #The door

    pygame.draw.ellipse(screen, YELLOW, [x,50,150,150])
    #ra the sun god

    pygame.draw.polygon(screen, ROOF, [[250,400],[500, 200],[750,400]])
    pygame.display.flip()
    #Updates the display
    x-=1
    
    clock.tick(FPS)



pygame.quit()
sys.exit()