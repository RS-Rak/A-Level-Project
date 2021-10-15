import pygame, sys
from pygame.locals import *

pygame.init()
#Initialises pygame. 

BLACK = (0,0,0)
WHITE = (255,255,255)
#OOOOH COLOURS

FPS = 60 #frames per second setting 

screenWidth = 1200
screenHeight = 900
# screen height and width in pixels, its like this for pure convenience. 

screen = pygame.display.set_mode((screenWidth,screenHeight))
# Makes a display window the size of my monitor. 

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
y_speed = 0

# Current position
y_coord = 350
while not done: #This is the main game loop - where all the magic happens babbyyyy
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_UP:
                if y_coord < 0:
                    y_coord = 1
                    y_speed = 0
                elif y_coord > 700:
                    y_coord = 700
                    y_speed = 0
                else:    
                    y_speed = -3
            elif event.key == pygame.K_DOWN:
                if y_coord > 700:
                    y_coord = 700
                    y_speed = 0
                elif y_coord < 0:
                    y_coord = 0
                    y_speed = 0
                else:
                    y_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
                if y_coord > 700:
                    y_coord = 700
                elif y_coord < 0:
                    y_coord = 0
    #game logic


    screen.fill(BLACK)
    #Fills screen with my colour of choice

    pygame.draw.rect(screen, WHITE, [0,y_coord,10,200])
    #Left paddle
    pygame.draw.rect(screen, WHITE, [1190,350,10,200])
    #Right Paddle
    pygame.draw.line(screen, WHITE, [600,0],[600,900],5)
    #Middle line
    pygame.display.flip()
    
    #Updates the display
    y_coord += y_speed
    clock.tick(FPS)



pygame.quit()
sys.exit()