
from states.state import State
from states.save_selection import *
from states.ingame_states.world import *
from states.Widgets.button import *
from states.menus import *
import pygame as pg
import os

class Menu(State):
    
    def __init__(self, game):
        State.__init__(self,game)
        #self.button_list = [] # list of buttons
        self.playbutton = TextButton(self.game, (self.game.GAME_W/2, self.game.GAME_H * 0.55), "PLAY", 
                                      (132,126,135), (255,255,255), bg_color=(34,32,52))
        self.optionbutton =  TextButton(self.game, (self.game.GAME_W/2, self.game.GAME_H * 0.7), "OPTIONS", 
                                        (132,126,135), (255,255,255), bg_color=(34,32,52))
        self.creditbutton = TextButton(self.game, (self.game.GAME_W/2, self.game.GAME_H * 0.85), "CREDITS", 
                                        (132,126,135), (255,255,255), bg_color=(34,32,52))
        self.button_list = [self.playbutton, self.optionbutton, self.creditbutton] 
        self.menu_img = pg.image.load(os.path.join(self.game.background_dir, "menu-background.png")).convert()
        self.logo_img = pg.image.load(os.path.join(self.game.icon_dir, "main-menu-logo.png")).convert()
        #dict for searching which button connects where 
        self.button_id = {
            0: Save_Selection(self.game, self.menu_img),
            1: Option(self.game, self.menu_img),
            2: Credits(self.game, self.menu_img)
        }
        
        
    def update(self, delta_time, actions):
        self.mouse_pos = pg.mouse.get_pos()
    
        for i in range(len(self.button_list)):
            self.button_list[i].checkCol(self.mouse_pos, actions)
            if self.button_list[i].clicked:
                new_state = self.button_id[i]
                new_state.enter_state()
                break
        
        if actions['return']:
            self.exit_state()
        self.game.reset_keys()
    
    def render(self, display):
        display.fill((255,255,255))
        display.blit(self.menu_img, (0,0))
        display.blit(self.logo_img, (self.game.GAME_W/2 - self.logo_img.get_rect().w/2, 0))
        for button in self.button_list:
            display.blit(button.image, (button.rect.x , button.rect.y))

       
