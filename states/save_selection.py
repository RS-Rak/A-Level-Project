from states.state import *
from states.Widgets.button import *
from Utility.util import *
from Utility.data import *
from states.ingame_states.world import *
import os

class Save_Selection(State):
    #this is for the save selection screen
    def __init__(self, game, menu_img):
        State.__init__(self, game)
        self.menu_img = menu_img
        self.save_slots = []
        self.button_list = []
        self.font = pg.font.Font(os.path.join(self.game.font_dir, "m6x11.ttf"), 20)
        for i in range(3):
            self.save_slots.append(ImageButton((self.game.GAME_W/2, 75 + i*50), "default-save-slot.png", 
                                               "default-save-slot-hover.png", self.game , os.path.join("assets","buttons","save-menu")))
        for i in range(3):
            self.button_list.append(TextButton(self.game, (self.game.GAME_W/2 - 25, 85 + i* 50), "PLAY", (132,126,135), (255,255,255), font=self.font))
            self.button_list.append(TextButton(self.game, (self.game.GAME_W/2 + 38, 85 + i* 50), "DELETE", (132,126,135), (255,255,255), font=self.font))
        self.save_dir = os.path.join("assets","saved_data","save_slots")
        
    def reset_save_slot(self, index):
        clear_save(index, default_data())
           
    def update(self, delta_time, actions):
        if actions['return']:
            self.exit_state()
            
        for i in range(3):
            self.save_slots[i].checkCol(pg.mouse.get_pos(), actions)
            if self.save_slots[i].hover == True:
                for x in range(6):
                    self.button_list[x].checkCol(pg.mouse.get_pos(), actions)
                    if self.button_list[x].clicked == True:
                        if x%2 == 0:
                            self.game.save_data = load_data(i, True)
                            self.game.save_slot = i+1
                            new_state = World(self.game, self.menu_img)
                            new_state.enter_state()
                        else:
                            self.reset_save_slot(i)
                
        self.game.reset_keys()
    
    def render(self, display):
        display.fill((255,255,255))
        display.blit(self.menu_img, (0,0))
        for i in range(3):
            display.blit(self.save_slots[i].image, (self.save_slots[i].rect.x, self.save_slots[i].rect.y))
            
            if load_data(i, True)["save-logo"] != None: #displays the location image with some dictionary wizadry. 
                display.blit((load_data(i, True))["save-logo"], (self.save_slots[i].rect.x + 4, self.save_slots[i].rect.y + 2))
                
        for i in range(6):
            display.blit(self.button_list[i].image, (self.button_list[i].rect.x, self.button_list[i].rect.y))
        
    
    def render_text(self, display):
        for i in range(3):
            self.game.draw_text(None, load_data(i, True)['name'], (255,255,255), (self.save_slots[i].rect.x + 80) , (self.save_slots[i].rect.y + 20), self.game.font)
            self.game.draw_text(None, convert_time(load_data(i, True)['time-played']), (255,255,255), self.save_slots[i].rect.x + 160, self.save_slots[i].rect.y + 20, self.game.font)
        self.game.draw_text(None, "SELECT A SAVE SLOT", (255,255,255), self.game.GAME_W/2,38, self.game.alt_font)