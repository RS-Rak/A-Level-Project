import time
import pygame as pg
from states.state import State
from states.UI.button import *
from Utility.util import *
from Utility.item_id import *
import os 
#inventory screen, visuals will be overhualed soon. additonal note, add stacking + ability to move items within it. 
class Inventory(State):
        
    def __init__(self, game):
        State.__init__(self, game)
        self.image = pg.image.load(os.path.join(self.game.assets_dir, "in-game", "finalinventory.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.GAME_W/2, self.game.GAME_H/2)
        self.inventory = self.game.save_data["inventory"]
        self.slot_list =[]
        self.x_offset, self.y_offset = 0,0
        self.currently_held = None
        for i in range(42):
            slot = Button(self.rect.x + 19 + self.x_offset * 23, self.rect.y + 15 + self.y_offset * 23, "inventory-slot.png", "inventory-slot-hover.png",self.game,"in-game", "topleft") #creates  buttons over inventory slots so i can tell when they're pressed. 
            self.slot_list.append(slot)
            self.x_offset += 1
            if (i+1)%6 == 0:
                self.y_offset += 1
                self.x_offset = 0  
            
        #print(self.inventory)
    
    def update(self, delta_time, actions):
        if actions['return'] or actions["inventory"]:
            self.game.save_data["inventory"] = self.inventory
            self.exit_state()
        for i in range(len(self.slot_list)):
            self.slot_list[i].checkCol(pg.mouse.get_pos(), actions, self.game)
            if self.slot_list[i].clicked == True:
                pass
        self.game.reset_keys()
    
    def render(self, display):
        display.blit(self.image, (self.rect))
        self.y_offset = 0
        self.x_offset = 0
        for i in range(42):
            display.blit(self.slot_list[i].image, (self.slot_list[i].rect))
            if self.inventory[str(i + 1)] == "000":
                pass
            else:
                display.blit(pg.image.load(item_dict[self.inventory[str(i+1)]]["item_image"]).convert_alpha(), (21 + (self.x_offset * 23) + self.rect.x, 17 + (self.y_offset * 23) + self.rect.y)) 
            
            if (i+1)%6 == 0:
                self.y_offset += 1
                self.x_offset = 0  
            self.x_offset += 1
            
       
            
            
    def display_tooltip(self, index,x,y): #displays a tooltip of the 
        self.tooltip_list = []
        if self.inventory[index] == '000':
            pass
        else:
            tooltip_surf = self.word_wrap(item_dict[self.inventory[index]]["item_tooltip"], self.game.small_font, (255,255,255), 0,0,200)
            font_width, font_height = self.game.small_font.size(str(item_dict[self.inventory[index]]["item_name"]))
            new_surf = pg.Surface((tooltip_surf.get_rect().w, tooltip_surf.get_rect().h + font_height + 10)) 
            new_surf.fill((25,38,56))
            self.text_render(new_surf, tooltip_surf.get_rect().w/2, 0, self.game.small_font,str(item_dict[self.inventory[index]]["item_name"]), (139,45,86))
            new_surf.blit(tooltip_surf, (0,font_height + 10))
            self.game.screen.blit(new_surf, (x,y))
        

    def text_render(self, screen, x,y, font, text, color):    
        text_surface = font.render(text, False, color)
        #text_surface.set_colorkey((0,0,0)) #this is for transparent fonts
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        screen.blit(text_surface, text_rect)
    
    def render_text(self):
        #I'm not actually using render text here to render - however, due to the way I've set up my game loop, if i want to render anything onto the full screen, I have to do it here rather than in the main render function, else it won't be rendered properly. 
        for i in range(len(self.slot_list)):
            if time.time() - self.slot_list[i].hover_time > 1 and self.slot_list[i].hover_time != 0:
                self.display_tooltip(str(i+1), pg.mouse.get_pos()[0] + 5, pg.mouse.get_pos()[1] + 5)
                
