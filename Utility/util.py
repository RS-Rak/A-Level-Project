from Utility.data import default_data
from Utility.text import Text
import json
import os
import pygame
import time
from datetime import datetime

#this file is mostly for json data manipulation. 


def get_logos(ID):
    logos = {
        "snowy-land": pygame.image.load(os.path.join("assets", "icons", "snowy-land.png")).convert(),
        "hidden-forest": pygame.image.load(os.path.join("assets", "icons", "forest.png")).convert()  
    }
    return logos[ID]

def set_save_logo(data):
    if data["current-location"] != "grandma's-temple":
        try:
            data['save-logo'] = get_logos(data["current-location"])
        except:
            pass
        
def clear_save(index, data):
    with open((os.path.join("assets","saved_data","save_slots","save_slot_{}.json".format(str(index + 1)))),'w') as file:
        json.dump(data, file)

def load_data(path, is_save = False):
    if is_save:
        with open((os.path.join("assets","saved_data","save_slots","save_slot_{}.json".format(str(path + 1)))),'r+') as file:
            data = json.load(file)
        set_save_logo(data)
    else:
        with open(path, 'r+') as file:
            data = json.load(file)
    return data

def dump_data(data, file_path):
    with open (file_path, 'w') as file:
        file.close()
    with open (file_path, 'r+') as file:
        json.dump(data, file)
    

def convert_time(time):
    #converts time into a hh:mm:ss format. time should be given in milliseconds.  
    time = time//1 #this converts it into whole seconds. 
    minutes = time//60
    seconds = int(time - (minutes * 60))
    hours = int(minutes//60)
    minutes = int(minutes - (hours * 60))
    if len(str(minutes)) < 2:
        minutes = "0" + str(minutes)
    if len(str(seconds)) < 2:
        seconds = "0" + str(seconds)
    if len(str(hours)) < 2:
        hours = "0" + str(hours)
    return "{} : {} : {}".format(str(hours), str(minutes), str(seconds))

def ConsoleOutput(message):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return f"[{now}] " + message

def debug(info, font, display, x=10, y=10):
    debug_surf = Text(font, info, 500, (255,255,255), None, (255,255,255), (0,0,0), (0,0,0))
    display.blit(debug_surf.image, (x,y))
    

class Timer():
    def __init__(self, time, trigger):
        self.timer = time 
        self.timer_started = False
        self.timer_finished = False
        self.trigger = trigger
                
    def start_timer(self): 
        self.start_time = time.time()
        self.timer_started = True
    
    def update(self):
        if time.time() - self.start_time >= self.timer:
            try : eval(self.trigger)
            except: pass
            self.timer_finished = True
    #note, maybe add a continuous timer? food for thought. 


