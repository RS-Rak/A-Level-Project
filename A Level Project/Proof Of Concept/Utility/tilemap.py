import pytmx
import pygame as pg 
from states.ingame_states.player import *

class TiledMap(pg.sprite.Sprite):
    def __init__(self, filename):
        pg.sprite.Sprite.__init__(self)
        self.tiledmap = pytmx.load_pygame(filename, pixelalpha = True)
        self.width = self.tiledmap.width * self.tiledmap.tilewidth
        self.height = self.tiledmap.height * self.tiledmap.tileheight
        self.collision_layer = self.tiledmap.get_layer_by_name('collisions')
        self.collision_tiles = []
        self.player = ''
        self.image = ''
        for x, y, tile in self.collision_layer.tiles():
            if (tile):
                self.collision_tiles.append(pg.Rect([(x* self.tiledmap.tilewidth), (y*self.tiledmap.tileheight), self.tiledmap.tilewidth, self.tiledmap.tileheight]));
    
    def render(self, surface):
        get_ti = self.tiledmap.get_tile_image_by_gid
        for layer in self.tiledmap.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = get_ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tiledmap.tilewidth, y * self.tiledmap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup):
                for object in layer:
                    if (object.name == 'Player'):
                        self.player = Player(object.x, object.y)
    
    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        self.image = temp_surface
        return temp_surface
    
    def update(self):
        pass
 
class Camera():
    def __init__(self, width, height):
        self.camera = pg.Rect(0,0,width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)
    
    def update(self, target, game):
        x = -target.rect.x + int(game.GAME_W/2)
        y = -target.rect.y + int(game.GAME_H/2)
        
        x = min(0,x)
        y = min(0,y)
        x = max(-(self.width - game.GAME_W), x)
        y = max(-(self.height - game.GAME_H), y)
        
        self.camera = pg.Rect(x,y,self.width, self.height)
               
