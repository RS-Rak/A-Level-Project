import pygame as pg
import time
from states.state import *
from states.pause_menu import *
from Utility.tilemap import *
from Utility.util import *
from states.ingame_states.inventory import *
from sprites.player import *
from sprites.chest import Chest

class Game_World(State):
    def __init__(self, game, menu_img):
        State.__init__(self, game)
        
    
        self.menu_img = menu_img
        self.all_sprites = pg.sprite.Group()
        self.start_time = time.time()
        
        self.map_dir = os.path.join("assets", "map")
        
        self.playerx = self.game.save_data["playerx"]
        self.playery = self.game.save_data["playery"] #loads the saved player location data. 
        self.get_tilemap()
         
        self.transparent_screen = pg.Surface((self.game.GAME_W, self.game.GAME_H))
        self.transparent_screen.set_alpha(180)
        self.transparency = False
        
    
    def get_tilemap(self):
        self.map_path = os.path.join(self.map_dir, str(self.game.save_data["current-map"]) + ".tmx")

        self.map = TiledMap(self.map_path, self.game)

        #self.spawn_data = load_data(os.path.join(self.map_dir,"spawn_data",str(self.game.save_data["current-map"]) + ".json"), False)
        self.collision_tiles = self.map.collision_tiles
        
        self.exits = self.map.exits
        self.exit_names = self.map.exits_names
        
        self.player = Player(self.playerx, self.playery, self.game)
        self.map.image = self.map.make_map()
        self.map.rect = self.map.image.get_rect()
        
        #self.all_sprites.add(self.map)
        self.all_sprites.add(self.player)
        self.camera = Camera(self.map.width, self.map.height)
        self.spawn_entities()
      
        
    def spawn_entities(self):
        self.chest_list = []
        for i in range(len(self.map.spawns)):
            if self.map.spawns[i].type == "Chest":
                new_chest = Chest(self.game, self.map.spawns[i].x, self.map.spawns[i].y, self.map.spawns[i].name)
                self.chest_list.append(new_chest)
                self.collision_tiles.append(new_chest)
                
    
    def get_player_location(self, map, prevmap): #gets the player location on the newmap
        self.spawn_data = load_data(os.path.join(self.map_dir,"spawn_data",str(map) + ".json"), False)
        self.playerx = self.spawn_data[str(prevmap)]["playerx"]
        self.playery = self.spawn_data[str(prevmap)]["playery"]
        self.game.save_data["playerx"] = self.playerx
        self.game.save_data["playery"] = self.playery
    
    def get_rel_player_loc(self): #gets the relative player location to the top left corner of the map. 
        map_x  = abs(self.map.rect.x)
        map_y = abs(self.map.rect.y)
        player_loc = (self.player.rect.x - map_x, self.player.rect.y - map_y)
        return player_loc
      
    def update(self, delta_time, actions):
        if actions['return']:
            self.transparency = True
            self.render(self.game.game_canvas)
            new_state = Pause_Menu(self.game, self.menu_img, self.start_time, self.get_rel_player_loc())
            self.game.reset_keys()
            new_state.enter_state()
            
        if actions["inventory"]:
            self.transparency = True
            self.render(self.game.game_canvas)
            new_state = Inventory(self.game)
            self.game.reset_keys()
            new_state.enter_state()
        
        if actions["interact"]:
            collision_rect = self.player.rect.inflate(3,3)
            for i in range(len(self.chest_list)):
                if collision_rect.colliderect(self.chest_list[i]):   
                    self.transparency = True
                    self.render(self.game.game_canvas)
                    new_state = ChestInventory(self.game, self.chest_list[i].data)
                    self.game.reset_keys()
                    new_state.enter_state()
        
          
        self.player.update(actions, delta_time, self.collision_tiles)
        changingMap, index = self.player.check_col(self.exits)
        
        if changingMap:
            self.get_player_location(self.exit_names[index], str(self.game.save_data["current-map"]))
            self.game.save_data["current-map"] = self.exit_names[index]
            self.get_tilemap()
        #self.game.reset_keys()
    
    def render(self, display):
        display.fill((0,0,0))
        #self.all_sprites.update()
        self.camera.update(self.player, self.game)
        for i in range(len(self.exits)):
            self.camera.apply_rect(self.exits[i])
            
        for tile in self.map.collision_tiles:
            display.blit(tile.image, self.camera.apply(tile))
        display.blit(self.map.image, self.camera.apply(self.map))
        for chest in self.chest_list:
            display.blit(chest.image, self.camera.apply(chest))
        for sprite in self.all_sprites:
            display.blit(sprite.image, self.camera.apply(sprite))
        if self.transparency == True:
            display.blit(self.transparent_screen, (0,0))
            self.transparency = False
        
        
        

        