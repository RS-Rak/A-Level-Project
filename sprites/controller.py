from sprites.animation import * 
import pygame as pg
import os
from Utility.util import *

#This is the controller class - it handles all of the actions and decides what to do with it. 

class Controller():
    def __init__(self, actions) -> None:
        pass
    


#While the event handler in game.py gives the player their movement and attacks, we need to consider how the enemies will handle theirs.
class EnemyController():
    def __init__(self, 
                 attack, 
                 curr_direction = "right", 
                 mode = "idle",
                 path = None
                 
            ):
        self.actions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "attack": False,
            "alt-attack":False
        } #this is the action dict for the AI
        self.attacks = {
            #this is an simple dict for now, but if i have any attacks which require special effects (such as a projectile, I want the attack info to be here)
            "attack": attack
        }
        self.modes = { #These are the AI "modes", and determine what actions it takes.
            "idle": False, 
            "set-path": False,
            "wandering": False,
            "attacking": False
        }
        
    def make_decision(self, player): #this function allows the AI to choose what action to take next
        if self.modes["idle"]:
            return 
        
    
class Animation(): #this loads up and splits up the great sprite sheet 
    def __init__(self, name) -> None:
        self.name = name   
        self.lists = { #this holds the image lists for each type of action 
            "left": [],
            "right": [],
            "up": [], 
            "down": [],
            "attack": [], 
        }
    
    def load_spritesheet(self):
        #loads the initial spritesheet, and then loads the data for cutting it up 
        self.spritesheet = os.path.join("assets", "sprites", "{}.png".format(str(self.name)))  
        self.spritesheet_data =  load_data(os.path.join("assets", "saved_data","animation_data","{}.json".format(str(self.name))))