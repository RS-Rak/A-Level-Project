"""

So, here I'm trying to see if resolution scaling is feasible for my future projects, and if it is, I'd like to explore it more, because being limited to one resolution in pygame is very unsatisfying. 

Here's my idea for it.

1. Take the input for the user's desired resolution size - could be implemented via input box, or scroll menu, or a million different ways depending on the game

2. Change a variable representing the scale factor - so that when I draw my sprites, they are scaled as well. 

2a. Or, use the pygame.transform.scale feature as soon as I figure out how the hell that works. 

Only issue is that this method might cause some image quality issues, so an alternative one is:

1. Take the resolution as before

2. Blit the sprites/image/drawings to a screen with the highest resolution you're willing to support. 

3. Use pygame.transform.scale to downscale. 




AFTER TESTING

Ok, so firstly I can just cut out the middle man and make it fullscreen immediately. This is pretty simple, and I am disappointed I have wasted so much time on this. 

"""

#Alright, pygame time. First, let's make a function for creating the screen. 
# Actually, since I want to create a text writer to the screen, alongside a test image I'm going to need a function for that jesus this is getting complex 




#The default pygame setup. Nothing truly special.

import pygame, sys
from pygame import display
from pygame.locals import *
from pygame.font import Font
from pygame.transform import scale

pygame.init() # INITALISES PYGAME
pygame.font.init() #INITALISES THE FONT 

fpsClock = pygame.time.Clock()
FPS = 30 #FPS constant, just so it's easier to check. 

#-------COLOURS------#
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# if a programmer suffers in the comments, and no one is there to read it, did it ever really happen?



#declare x and y, which are the dimensions of the screen
X = 800
Y = 600

#So what this bit does, is it gets the display info of the user's screen, so I can set an automatic first 
displayStats = pygame.display.Info()
displayHeight = displayStats.current_h
displayWidth = displayStats.current_w

#Loads the image, a beautiful, beautiful kekw. 
image = pygame.image.load("resolution/kekw-emote-twitch.jpg")
#Ana also we're gonna scale it up a bit, it's kinda small. 
image = pygame.transform.scale(image, (450,450))

#sets up the screen. HWSURFACE AND DOUBLEBUF do some more stuff to help performance. 
screen = pygame.display.set_mode((X,Y),HWSURFACE|DOUBLEBUF|RESIZABLE)

#Now, we're going to do some wild things - in order to scale everything on the screen, we're going to create a copy of the screen.
scaled_screen = screen.copy()

#Fills the screen with black
screen.fill(BLACK)
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        #If the user attempts to resize the video in anyway, then it does this 
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
        elif event.type == KEYDOWN:
            if event.key == K_x:
                running = False

        #Gets the current resolution
        displayStats = pygame.display.Info()
        displayHeight = displayStats.current_h
        displayWidth = displayStats.current_w
        displayHW = (displayWidth,displayHeight)
        
        #I want to display some text showing the resultion
        text = ("The resolution is: {}".format(str(displayHW)))
        
        #Renders text
        font = pygame.font.Font("resolution/Fonts/Thin.ttf", 24)
        text = font.render(text, 1, pygame.Color(WHITE))
        

        #Gets the rough dimensions of the text box
        tWidth = text.get_rect().width
        tHeight = text.get_rect().height

        #Same for the image
        iWidth = image.get_rect().width
        iHeight = image.get_rect().height
        
        #-------DRAWING CODE -----#



        #FILLS SCREEN
        scaled_screen.fill(BLACK)

        #BLITS THE TEXT AND IMAGE TO THE SCALED SCREEN, CENTERS THEM
        scaled_screen.blit(text,((X - tWidth)/2,(Y - tHeight)))
        scaled_screen.blit(image, ((X - iWidth)/2,(Y - iHeight)/2))

        #Scaling time, what it does is it scales up the false screen, gets the current dimensions of the screen, scales it up, and blits it on. 
        screen.blit(pygame.transform.scale(scaled_screen, screen.get_rect().size), (0,0))

        pygame.display.flip()
        fpsClock.tick(FPS)

pygame.exit()
sys.exit()
