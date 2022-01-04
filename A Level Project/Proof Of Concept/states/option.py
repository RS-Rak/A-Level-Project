import json
import pygame as pg
from states.state import State
from states.UI.button import *
from Utility.util import *
class Option(State):
    
    def __init__(self, game, menu_img):
        State.__init__(self, game)
        self.menu_img = menu_img
    
    def update(self, delta_time, actions):
        if actions['return']:
            self.exit_state()
        self.game.reset_keys()
    
    def render(self, display):
        display.fill((255,255,255))
    
    def render_text(self):    
        self.game.draw_text(None, "OPTIONS TO BE ADDED", (0,0,0), self.game.GAME_W/2, self.game.GAME_H * 0.35, self.game.font)
        
class Credits(State):
    def __init__(self, game, menu_img):
        State.__init__(self, game)
        self.menu_img = menu_img
    
    def update(self, delta_time, actions):
        if actions['return']:
            self.exit_state()
        self.game.reset_keys()
    
    def render(self, display):
        display.fill((255,255,255))
    
    def render_text(self):
        self.game.draw_text(None, "CREDITS TO BE ADDED", (0,0,0), self.game.GAME_W/2, self.game.GAME_H * 0.35, self.game.font)


        

