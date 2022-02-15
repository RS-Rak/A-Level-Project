import pygame as pg
from states.state import State
from states.Widgets.button import *
import time
import copy 
from Utility.data import *
from Utility.text import Text
import os 

class InventoryManager(State):
    def __init__(self, game, inv_type):
        State.__init__(self, game)
        
        if inv_type == 'Inventory':
            self.image = pg.image.load(os.path.join(self.game.assets_dir, "in-game", "inventory.png")).convert_alpha()
        else:
            self.image = pg.image.load(os.path.join(self.game.assets_dir, "in-game", "inventory-chest.png")).convert_alpha()
            
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.GAME_W/2, self.game.GAME_H/2)
        self.inventory = self.game.save_data["inventory"]
        self.current_inv = self.inventory[self.inventory["Current-Inv"]]
        self.currently_held = None
        
        self.tab_list = {
            "item-tab":Tab((self.rect.x, self.rect.y + 27), "item-tab.png", "item-tab-hover.png", self.game, os.path.join("assets", "buttons","in-game"),
                          "topleft", "item-tab-clicked.png", "item-inv"),
            "equipment-tab":Tab((self.rect.x, 74 + self.rect.y), "equipment-tab.png", "equipment-tab-hover.png", self.game, os.path.join("assets", "buttons","in-game"), 
                               "topleft", "equipment-tab-clicked.png","equipment-inv"),
            "spells-tab": Tab((self.rect.x, 121 + self.rect.y), "spells-tab.png", "spells-tab-hover.png", self.game, 
                              os.path.join("assets", "buttons","in-game"), "topleft", "spells-tab-clicked.png", "spells-inv")
        }
        
        for i in self.tab_list:
            if i == self.inventory["Current-Inv"]:
                self.tab_list[i].selected = True
        
        self.x_offset, self.y_offset = 0,0       
        self.slot_list = []
        self.equipment, self.equipped_spells, self.equipped_armour = [], [], []
        for i in range(48):
            slot = ImageButton((self.rect.x + 21 + self.x_offset * 23, self.rect.y + 12 + self.y_offset * 23), "inventory-slot.png", 
                        "inventory-slot-hover.png",self.game,os.path.join("assets", "buttons","in-game"), "topleft", "all")
            self.slot_list.append(slot)
            self.x_offset += 1
            if (i+1)%6 == 0:
                self.y_offset += 1
                self.x_offset = 0
        
        self.all_slots = [self.slot_list, self.equipment, self.equipped_spells, self.equipped_armour] 
        self.item_list = self.load_items()
        #self.load_images(inv_type)
        
    def update(self, delta_time, actions):
        if actions['return'] or actions["interact"] or actions["inventory"]:
            self.game.save_data["inventory"] = self.inventory
            self.exit_state()
            
        for i in range(len(self.all_slots)):
            for x in range(len(self.all_slots[i])):
                self.all_slots[i][x].checkCol(pg.mouse.get_pos(), actions)
                if self.all_slots[i][x].clicked == True:
                    pass
                #self.current_inv[i] 
            
        for i in self.tab_list:
            if self.tab_list[i].selected != True:
                self.tab_list[i].checkCol(pg.mouse.get_pos(), actions)
                if self.tab_list[i].selected == True:
                    for x in self.tab_list:
                        self.tab_list[x].selected = False
                    self.tab_list[i].selected = True 
                    self.current_inv = self.inventory[self.tab_list[i].name] 
                    self.item_list = self.load_items()
                    self.inventory["Current-Inv"] = self.tab_list[i].name
        self.game.reset_keys()
    
    
    def load_items(self):
        item_list = []
        for i in self.current_inv:
            if self.current_inv[i] == "000": pass 
            else: 
                item = copy.deepcopy(item_dict[self.current_inv[i]])
                item.set_loc((self.slot_list[int(i) - 1].rect.x + 11, self.slot_list[int(i)].rect.y + 11))
                item_list.append(item)
        return item_list
    
    def render(self, display):
        display.blit(self.image, (self.rect))     
        self.render_list(self.slot_list, display)
        self.render_dict(self.tab_list, display)
        self.render_list(self.item_list, display)

    def display_tooltip(self, index,x,y): #displays a tooltip of the 
        self.tooltip_list = []
        if self.current_inv[index] != '000':
            tooltip = Text(self.game.small_font, item_dict[self.current_inv[index]].tooltip, 200, (255,255,255), 
                           item_dict[self.current_inv[index]].name, (193,45,86),(0,0,0), (25,38,56))
            self.game.screen.blit(tooltip.image, (x,y))
    
    def render_text(self, display):
        #I'm not actually using render text here to render - however, due to the way I've set up my game loop, if i want to render anything onto the full screen, I have to do it here rather than in the main render function, else it won't be rendered properly. 
        for i in range(len(self.slot_list)):
            if time.time() - self.slot_list[i].hover_time > 1 and self.slot_list[i].hover_time != 0:
                self.display_tooltip(str(i+1), pg.mouse.get_pos()[0] + 5, pg.mouse.get_pos()[1] + 5)
