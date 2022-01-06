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