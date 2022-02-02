import pygame as pg 
import os

class Item():
    def __init__(self, name, image, itemtype, subtype,damage, effect, tooltip):
        self.name = name
        self.path = image
        
        self.type = itemtype
        self.subtype = subtype
        self.damage = damage
        self.effect = effect
        self.tooltip = tooltip
        
    
    def set_loc(self, loc):
        self.image = pg.image.load(self.path)
        self.rect = self.image.get_rect()
        self.rect.center = loc
    
#this entire file serves purely as an item dictionary for my various items,
item_dict = {
    "000": None,
    "001": Item("Simple Sword", os.path.join("assets","icons","Swords","default-sword.png"), "Equipment", "Sword", 5, None, 
                "A simple blade, the kind that you'd see wielded by merchant's guards. ")
    ,
    "002":  Item("Healing Potion", os.path.join("assets", "icons", "Potions","healing-potion.png"), "Item", "Potion", 5, "Healing", 
                 "A simple healing potion, crafted with the most basic of magics." )  
}
enemy_dict = {
    "player": {
        "HP": 400,
        "ATTACK-SPEED": 8,
        "ENTITY-SPEED": 100,
    } 
}
"""
format below:

"item_name": "",
"item_image": ""
"item_type": "",
"item_damage": "" ,
"item_effect": "",
"item_tooltip": ""

"""