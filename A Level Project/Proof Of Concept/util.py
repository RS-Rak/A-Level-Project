import json, os, pygame
from pygame.event import clear
def default_data():
    data = {
        "time-played":0,
        "name": "???",
        "save-logo": None,
        "current-location": "grandma's-temple",
        "cutscenes": {
            "opening-cutscene": False,
            "book-discovery": False,
        #I'll add more cutscene names here as I go. See cutscene- notes.txt for more info 
            
        },
        "inventory": {
            "EquippedWeapon": "0001",
            "EquippedArmor":"0002",
            "Hitpoints": 10,
            "Mana": 10,
            "Ability1": "0000",
            "Ability2": "0000",
            "Ability3": "0000",
            "Ability4": "0000",
            "Ultimate": "0000",
            1: "0000",
            2: "0000",
            3: "0000",
            4: "0000",
            5: "0000",
            6: "0000",
            7: "0000",
            8: "0000",
            9: "0000",
            10:"0000",
            11:"0000",
            12:"0000",
            13:"0000",
            14:"0000",
            15:"0000",
            16:"0000",
            17:"0000",
            18:"0000",
            19:"0000",
            20:"0000",
            21:"0000",
            22:"0000",
            23:"0000",
            24:"0000",
            25:"0000",
            26:"0000",
            27:"0000",
            28:"0000",
            29:"0000",
            30:"0000",   }  
    }
    return data

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

def load_data(index):
    with open((os.path.join("assets","saved_data","save_slots","save_slot_{}.json".format(str(index + 1)))),'r+') as file:
        data = json.load(file)
    set_save_logo(data)
    return data

def convert_time(time):
    #converts time into a hh:mm:ss format. time should be given in milliseconds.  
    time = time/1000
    time = time//1 #this converts it into seconds. 
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


    
#options to be added. 
#for i in range(3):
 #   clear_save(i, default_data())
#this is for resetting my json files. 