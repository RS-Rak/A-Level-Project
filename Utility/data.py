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
 
class Weapon(Item):
    def __init__(self, name, image, itemtype, subtype, damage, effect, tooltip):
        super().__init__(name, image, itemtype, subtype, damage, effect, tooltip)
       
#this entire file serves purely as an item dictionary for my various items,
item_dict = {
    "000": None,
    "001": Weapon("Simple Sword", os.path.join("assets","icons","Swords","default-sword.png"), "Melee", "Sword", 5, None, 
                "A simple blade, the kind that you'd see wielded by merchant's guards. ")
    ,
    "002":  Item("Healing Potion", os.path.join("assets", "icons", "Potions","healing-potion.png"), "Item", "Potion", 5, "Healing", 
                 "A simple healing potion, crafted with the most basic of magics." )  
}
entity_dict = {
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
def default_data():
    data = {
        "time-played":0,
        "name": "???",
        "save-logo": None,
        "current-location": "grandma's-temple",
        "current-map": "test-map",
        "playerx": 265,
        "playery": 298,
        "cutscenes": {
            "opening-cutscene": False,
            "book-discovery": False,
        #I'll add more cutscene names here as I go. See cutscene- notes.txt for more info 
            
        },
        "inventory": {
            "Current-Inv": "item-inv", 
            "EquippedWeapon": "001",
            "EquippedArmor":"000",
            "Hitpoints": 10,
            "Mana": 10,
            "Ability1": "000",
            "Ability2": "000",
            "Ability3": "000",
            "Ability4": "000",
            "Ultimate": "000",
            "item-inv":{
                 1: "002", 2: "000",3: "000", 4: "000", 5: "000", 6: "000", 7: "000", 8: "000", 9: "000", 10:"000", 11: "000", 12: "000",13: "000", 14: "000", 15: "000", 16: "000", 17: "000", 18: "000", 19: "000", 20:"000", 21: "002", 22: "000",23: "000", 24: "000", 25: "000", 26: "002", 27: "000", 28: "000", 29: "000", 30:"000",  31: "000", 32: "000",33: "002", 34: "000", 35: "000", 36: "000", 37: "000", 38: "000", 39: "000", 40:"000", 41: "000", 42: "000",43: "000", 44: "000", 45: "000", 46: "000", 47: "000", 48: "000"
                     },
            "equipment-inv":{
                 1: "001", 2: "000",3: "000", 4: "000", 5: "000", 6: "000", 7: "000", 8: "000", 9: "000", 10:"000", 11: "001", 12: "000",13: "000", 14: "000", 15: "000", 16: "000", 17: "000", 18: "000", 19: "000", 20:"000", 21: "001", 22: "000",23: "000", 24: "000", 25: "000", 26: "000", 27: "000", 28: "000", 29: "000", 30:"000",  31: "001", 32: "000",33: "000", 34: "000", 35: "000", 36: "000", 37: "000", 38: "000", 39: "000", 40:"000", 41: "001", 42: "000",43: "000", 44: "000", 45: "000", 46: "000", 47: "000", 48: "000"
                     },
            "spells-inv":{
                 1: "000", 2: "000",3: "000", 4: "000", 5: "000", 6: "000", 7: "000", 8: "000", 9: "000", 10:"000", 11: "000", 12: "000",13: "000", 14: "000", 15: "000", 16: "000", 17: "000", 18: "000", 19: "000", 20:"000", 21: "000", 22: "000",23: "000", 24: "000", 25: "000", 26: "000", 27: "000", 28: "000", 29: "000", 30:"000",  31: "000", 32: "000",33: "000", 34: "000", 35: "000", 36: "000", 37: "000", 38: "000", 39: "000", 40:"000", 41: "000", 42: "000",43: "000", 44: "000", 45: "000", 46: "000", 47: "000", 48: "000"
                     }
            }  
    }
    return data