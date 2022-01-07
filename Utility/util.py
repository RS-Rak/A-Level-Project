import json, os, pygame
#this file is mostly for json data manipulation. 

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
            "EquippedWeapon": "000",
            "EquippedArmor":"000",
            "Hitpoints": 10,
            "Mana": 10,
            "Ability1": "000",
            "Ability2": "000",
            "Ability3": "000",
            "Ability4": "000",
            "Ultimate": "000",
            1: "000",
            2: "000",
            3: "000",
            4: "000",
            5: "000",
            6: "000",
            7: "000",
            8: "000",
            9: "000",
            10:"000",
            11:"000",
            12:"000",
            13:"000",
            14:"000",
            15:"000",
            16:"000",
            17:"000",
            18:"000",
            19:"000",
            20:"000",
            21:"000",
            22:"000",
            23:"000",
            24:"000",
            25:"000",
            26:"000",
            27:"000",
            28:"000",
            29:"000",
            30:"000",
            31:"000",
            32:"000",
            33:"000",
            34:"000",
            35:"000",
            36:"000",
            37:"000",
            38:"000",
            39:"000", 
            40:"000",}  
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

def load_data(path, is_save):
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


#options to be added. 
#for i in range(3):
 #  clear_save(i, default_data())
#this is for resetting my json files. 

