from states.state import State
from states.UI.button import *
import pygame as pg
from states.option import Option

class Pause_Menu(State):
    #this is for the save selection screen
    def __init__(self, game, menu_img):
        State.__init__(self, game)
        self.img = menu_img
        self.image = pg.image.load(os.path.join(self.game.assets_dir, "buttons", "pause-menu", "pause-menu-frame.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.GAME_W/2, self.game.GAME_H/2)
        self.button_list = []
        self.button_list.append(Button(self.game.GAME_W/2, self.game.GAME_H/2 - 30,"resume-button.png", "resume-button-hover.png", self.game , "pause-menu"))
        self.button_list.append(Button(self.game.GAME_W/2, self.game.GAME_H/2, "option-button.png", "option-button-hover.png", self.game , "pause-menu"))
        self.button_list.append(Button(self.game.GAME_W/2, self.game.GAME_H/2 + 30, "quit-button.png", "quit-button-hover.png", self.game , "pause-menu"))
    
    
    
    def update(self, delta_time, actions):
        if actions['return']:
            self.exit_state()
            
        for i in range(len(self.button_list)):
            self.button_list[i].checkCol(pg.mouse.get_pos(), actions, self.game)
            if self.button_list[i].clicked == True:
                if i == 0:
                    self.exit_state()
                elif i == 1:
                    new_state = Option(self.game, self.img)
                    self.exit_state()
                    new_state.enter_state()
                else:
                    while len(self.game.state_stack) > 1:
                        self.game.state_stack.pop() 
                
        self.game.reset_keys()
    
    def render(self, display):
        
        display.blit(self.image, (self.rect.x, self.rect.y))
        for i in range(len(self.button_list)):
            display.blit(self.button_list[i].image,(self.button_list[i].rect.x, self.button_list[i].rect.y))
        
        