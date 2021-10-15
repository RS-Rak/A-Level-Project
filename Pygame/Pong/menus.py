import pygame
from random import randint
import time
from pygame import font

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

def write(text, color, size):
        if len(text) > 13:
            font = pygame.font.Font("Pygame/Pong/Fonts/arcade.TTF",size)
        else:
            font = pygame.font.Font("Pygame/Pong/Fonts/BACKTO1982.TTF",size)

        
        text = font.render(text, 1, pygame.Color(color))
        
        textWidth = text.get_rect().width
        textHeight = text.get_rect().height
        
        return text, textWidth, textHeight

class Menus():

    def main_menu(screen):
        
        screen.fill(BLACK)
        
        pygame.font.init()

        #This is going to be the main menu 
        text, textWidth, textHeight = write("PONG", WHITE, 144)
        screen.blit(text, (((700 - textWidth)/2),(400 - textHeight)/2))

        #This will be a small message under the the main screen thing. 
        text, textWidth, textHeight = write("Press 2 to enter 2P mode.", WHITE, 20)
        screen.blit(text, (((700 - textWidth)/2),(500 - textHeight)))

        text, textWidth, textHeight = write("Press 1 to enter 1P mode.", WHITE, 20)
        screen.blit(text, (((700 - textWidth)/2),(500 - textHeight * 2)))