import pytmx
import pygame as pg 


class TiledMap(pg.sprite.Sprite):
    def __init__(self, filename, game):
        pg.sprite.Sprite.__init__(self)
        self._layer = 1
        self.game = game
        self.tiledmap = pytmx.load_pygame(filename, pixelalpha = True)
        self.width = self.tiledmap.width * self.tiledmap.tilewidth
        self.height = self.tiledmap.height * self.tiledmap.tileheight
        self.collision_layer = self.tiledmap.get_layer_by_name('collisions')
        self.exit_layer = self.tiledmap.get_layer_by_name("Exits")
        self.collision_tiles = [] #collision tiles
        self.exits = [] #this is the exits for the map. 
        self.exits_names = [] #we alos need the name for the exits
        self.image = ''
        for x, y, tile in self.collision_layer.tiles(): #gets the collision tiles
            if (tile):
                new_tile = Collision_Tile(x * self.tiledmap.tilewidth, y * self.tiledmap.tileheight, self.tiledmap.tilewidth)
                self.collision_tiles.append(new_tile)
                
        for object in self.exit_layer: #gets the exit rects.
            new_rect = pg.Rect([object.x, object.y, object.width, object.height])
            self.exits_names.append(object.name)
            self.exits.append(new_rect)
        
    def render(self, surface):
        get_ti = self.tiledmap.get_tile_image_by_gid
        for layer in self.tiledmap.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = get_ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tiledmap.tilewidth, y * self.tiledmap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup) and (layer != self.exit_layer):
                for object in layer:
                    #ithis is where i'll put all the other object layers.  
                     pass
    
    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        self.image = temp_surface
        return temp_surface
    
    def update(self):
        pass
 
class Collision_Tile():
    def __init__(self, x, y, tilesize):
        self.image=pg.Surface((tilesize, tilesize))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    

 
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
        x = -target.rect.centerx + int(game.GAME_W/2)
        y = -target.rect.centery + int(game.GAME_H/2)
        
        x = min(0,x)
        y = min(0,y)
        x = max(-(self.width - game.GAME_W), x)
        y = max(-(self.height - game.GAME_H), y)
        
        self.camera = pg.Rect(x,y,self.width, self.height)
               
