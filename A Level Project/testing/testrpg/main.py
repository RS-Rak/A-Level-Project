import pygame
from config import *
from sprites import *
import sys

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Arial', 32)
        #determines if the program is running or not. 
        self.running = True
    
    def new(self):
        # a new game starts
        self.playing = True
    
    def update(self):
        #updates every so often 
        pass
    
    def draw(self):
        #draws everything to the screen.
        pass

    def main(self):
        #where all the magic happens.
        pass
    
    def game_over(self):
        #when you die, this runs 
        pass
    
    def intro_screen(self):
        #introduction.
        pass
    
        