import pygame as pg
import time
from states.state import *
from states.pause_menu import *
from Utility.tilemap import *
from states.ingame_states.inventory import *

class Game_World(State):
    def __init__(self, game, menu_img):
        State.__init__(self, game)
        self.menu_img = menu_img
        self.all_sprites = pg.sprite.Group()
        self.start_time = time.time()
        self.get_tilemap("assets/map/test-map.tmx")
        self.transparent_screen = pg.Surface((self.game.GAME_W, self.game.GAME_H))
        self.transparent_screen.set_alpha(180)
        self.transparency = False
    
    def get_tilemap(self, path):
        self.map = TiledMap(path)
        self.map.image = self.map.make_map()
        self.map.rect = self.map.image.get_rect()
        self.all_sprites.add(self.map)
        self.all_sprites.add(self.map.player)
        self.camera = Camera(self.map.width, self.map.height)
        
    def update(self, delta_time, actions):
        if actions['return']:
            self.transparency = True
            self.render(self.game.game_canvas)
            new_state = Pause_Menu(self.game, self.menu_img)
            new_state.enter_state()
        if actions["inventory"]:
            self.transparency = True
            self.render(self.game.game_canvas)
            new_state = Inventory(self.game)
            new_state.enter_state()
                
        self.game.reset_keys()
    
    def render(self, display):
        display.fill((0,0,0))
        self.all_sprites.update()
        self.camera.update(self.map.player, self.game)
        #all_sprites_list.draw(screen)

        for sprite in self.all_sprites:
            display.blit(sprite.image, self.camera.apply(sprite))

        
        
        
        if self.transparency == True:
            display.blit(self.transparent_screen, (0,0))
            self.transparency = False
        
        
        

        