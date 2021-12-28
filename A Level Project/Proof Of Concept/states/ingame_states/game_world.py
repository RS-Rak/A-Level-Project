import pygame as pg
from states.state import State
from states.pause_menu import *

class Game_World(State):
    def __init__(self, game, menu_img):
        State.__init__(self, game)
        self.menu_img = menu_img
       
    
    def update(self, delta_time, actions):
        if actions['return']:
            new_state = Pause_Menu(self.game, self.menu_img)
            new_state.enter_state()
            
        self.game.reset_keys()
    
    def render(self, display):
        display.fill((255,255,255))