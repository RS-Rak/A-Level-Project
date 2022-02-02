import copy
import pygame as pg
from states.Widgets.button import *
from Utility.util import *
from Utility.data import * 
from states.ingame_states.inventory_manager import InventoryManager


class Inventory(InventoryManager):
    def __init__(self, game):
        InventoryManager.__init__(self, game, "Inventory")
        self.load_images()
        
        
    def load_images(self):
        for i in range(4):
            self.equipped_armour.append(Slot(self.rect.x + 121, self.rect.y + 24 + i * 23, "equip-slot.png", 
                        "equip-slot-hover.png",self.game,"in-game", "topleft", "armour"))   
        for i in range(5):    
            self.equipped_spells.append(Slot(self.rect.x + 173 + i*25, self.rect.y + 172, "equip-slot.png", 
                        "equip-slot-hover.png",self.game,"in-game", "topleft", "spells"))
        for i in range(2):
            self.equipment.append(Slot(self.rect.x + 215 + i*25, self.rect.y + 133, "equip-slot.png", 
                        "equip-slot-hover.png",self.game,"in-game", "topleft", "equipment"))  
    
    def render(self,display):
        super().render(display)
        
    def update(self, delta_time, actions):   
        super().update(delta_time, actions)    
    
          
    def display_tooltip(self, index,x,y): #displays a tooltip of the 
        super().display_tooltip(index,x,y)
        

    def text_render(self, screen, x,y, font, text, color):    
        super().text_render(screen,x,y,font,text,color)
    
    def render_text(self):
        super().render_text()

class ChestInventory(InventoryManager):
    def __init__(self, game, chestinv):
        InventoryManager.__init__(self, game, "Chest")
        self.chest_inv = chestinv
        self.load_images()
        self.load_chest_items()
        
        
    def load_images(self):
        self.chest_slots = []
        self.x_offset, self.y_offset = 0,0
        for i in range(40):
            slot = Slot(self.rect.x + 181 + self.x_offset * 23, self.rect.y + 12 + self.y_offset * 23, "inventory-slot.png", 
                        "inventory-slot-hover.png",self.game,"in-game", "topleft", "all")
            self.chest_slots.append(slot)
            self.x_offset += 1
            if (i+1)%5 == 0:
                self.y_offset += 1
                self.x_offset = 0 
        self.all_slots.append(self.chest_slots)
    
    def load_chest_items(self):
        self.chest_items = []
        for i in self.chest_inv:
            if self.chest_inv[i] != "000":
                item = copy.deepcopy(item_dict[self.chest_inv[i]])
                item.set_loc((self.chest_slots[int(i) - 1].rect.x + 11, self.chest_slots[int(i)].rect.y + 11))
                self.chest_items.append(item)
    
    def render(self,display):
        super().render(display)
        self.render_list(self.chest_slots, display)
        self.render_list(self.chest_items, display)
        
    def update(self, delta_time, actions):   
        super().update(delta_time, actions)    
    
          
    def display_tooltip(self, index,x,y): #displays a tooltip of the 
        super().display_tooltip(index,x,y)
        

    def text_render(self, screen, x,y, font, text, color):    
        super().text_render(screen,x,y,font,text,color)
    
    def render_text(self):
        super().render_text()
         
