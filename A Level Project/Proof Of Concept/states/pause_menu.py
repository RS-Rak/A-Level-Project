from Utility.util import *
from states.state import State
from states.UI.button import *
import pygame as pg
from states.option import Option
import time
#this is my pause menu.

class Pause_Menu(State):
    
    def __init__(self, game, menu_img, start_time, player_loc):
        State.__init__(self, game)
        self.playerx = player_loc[0] #as you might see, i've saved data such as player location and time. this is to write to the json file in case the user quits to menu. 
        self.playery = player_loc[1]
        
        self.img = menu_img #
        self.image = pg.image.load(os.path.join(self.game.assets_dir, "buttons", "pause-menu", "pause-menu-frame.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.GAME_W/2, self.game.GAME_H/2) #centers the pause menu in the center of the screen.
        
        self.button_list = [] #these are my buttons, they're held in a list for convenience.
        self.button_list.append(Button(self.game.GAME_W/2, self.game.GAME_H/2 - 30,"resume-button.png", "resume-button-hover.png", self.game , "pause-menu"))
        self.button_list.append(Button(self.game.GAME_W/2, self.game.GAME_H/2, "option-button.png", "option-button-hover.png", self.game , "pause-menu"))
        self.button_list.append(Button(self.game.GAME_W/2, self.game.GAME_H/2 + 30, "quit-button.png", "quit-button-hover.png", self.game , "pause-menu"))
        self.start_time = start_time
    
    
    def update(self, delta_time, actions):
        if actions['return']: #
            self.exit_state()
            
        for i in range(len(self.button_list)):
            self.button_list[i].checkCol(pg.mouse.get_pos(), actions, self.game)
            if self.button_list[i].clicked == True: #if a button is clicked, it checks which one is clicked
                if i == 0: #resume
                    self.exit_state()
                elif i == 1: #options
                    new_state = Option(self.game, self.img)
                    self.exit_state()
                    new_state.enter_state()
                else: #quit to menu , saves all the data it can. 
                    self.game.save_data["time-played"] = self.game.save_data["time-played"] + (time.time() - self.start_time) #this saves the time played.
                    self.game.save_data["playerx"] = self.playerx #this saves the current co-ordinates of the player. 
                    self.game.save_data["playery"] = self.playery
                    try:
                        dump_data(self.game.save_data, os.path.join(self.game.assets_dir, "saved_data", "save_slots","save_slot_{}.json".format(str(self.game.save_slot))))
                    except: pass
                    while len(self.game.state_stack) > 1:
                        self.game.state_stack.pop() 
                
        self.game.reset_keys()
    
    def render(self, display):
        
        display.blit(self.image, (self.rect.x, self.rect.y))
        for i in range(len(self.button_list)):
            display.blit(self.button_list[i].image,(self.button_list[i].rect.x, self.button_list[i].rect.y))
        
        