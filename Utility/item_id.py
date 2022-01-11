import pygame as pg 
import os
#this entire file serves purely as an item dictionary for my various items,
item_dict = {
    "000": None,
    "001": {
        "item_name": "Simple Sword",
        "item_image": os.path.join("assets","icons","Swords","default-sword.png"),
        "item_type": "Sword",
        "item_damage": 5,
        "item_effect": None,
        "item_tooltip": "A simple blade, the kind that you'd see wielded by merchant's guards. "
    },
    "002": {
        "item_name": "Healing Potion",
        "item_image": os.path.join("assets", "icons", "Potions","healing-potion.png"),
        "item_type": "Item",
        "item_sub_type": "Potion",
        "item_damage": 0 ,
        "item_effect": "Healing",
        "item_tooltip": "A simple healing potion, crafted with the most basic of magics."
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