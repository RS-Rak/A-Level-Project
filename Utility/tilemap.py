import pytmx
import pygame as pg
from sprites.entity import Entity 
#This file is responsible for the creation of the tilemap. 

class TiledMap(Entity):
    def __init__(self, filename, game):
        super().__init__(game)
        
        self._layer = 1
        
        self.tiledmap = pytmx.load_pygame(filename, pixelalpha = True) #loads the file
        self.width = self.tiledmap.width * self.tiledmap.tilewidth
        self.height = self.tiledmap.height * self.tiledmap.tileheight
        
        self.collision_layer = self.tiledmap.get_layer_by_name('collisions') #grabs the collision layers
        self.exit_layer = self.tiledmap.get_layer_by_name("Exits")
        self.collision_tiles = [] #collision tiles
        self.exits = [] #this is the exits for the map. 
        self.exits_names = [] #we alos need the name for the exits
        self.spawns = []
        self.image = ''
        
        for x, y, tile in self.collision_layer.tiles(): #gets the collision tiles
            if (tile):
                new_tile = Collision_Tile(game, x * self.tiledmap.tilewidth, y * self.tiledmap.tileheight, self.tiledmap.tilewidth)
                self.collision_tiles.append(new_tile)
                
        for object in self.exit_layer: #gets the exit rects.
            new_rect = pg.Rect([object.x, object.y, object.width, object.height])
            self.exits_names.append(object.name)
            self.exits.append(new_rect)
        
    def render_image(self, surface): #renders the whole thing
        get_ti = self.tiledmap.get_tile_image_by_gid
        for layer in self.tiledmap.layers: #renders layer by layer, all in their relative position
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = get_ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tiledmap.tilewidth, y * self.tiledmap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup) and (layer != self.exit_layer):
                for object in layer:
                    self.spawns.append(object)
                    #print(object.name, object.x, object.y, object.type) #this is just so I can see the current location of all objects 
                    #ithis is where i'll put all the other object layers.  
                     
    
    def make_map(self): #renders it to a temp surface so i only need to manipulate the layer. Convenient right? 
        temp_surface = pg.Surface((self.width, self.height))
        self.render_image(temp_surface)
        self.image = temp_surface
        return temp_surface
    
    def update(self): #I had this here in case of using all.sprites.list.update - still gonna keep it just in case. 
        pass
 
class Collision_Tile(Entity): #collisiomn tiles are their own class so i can create a bunch easily. 
    def __init__(self, game, x, y, tilesize):
        super().__init__(game)
        self.image=pg.Surface((tilesize, tilesize))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    

 
class Camera():
    def __init__(self, width, height):
        self.camera = pg.Rect(0,0,width, height) #the camera represents what's actually being displayed on the screen at any given moment. 
        self.width = width
        self.height = height
    
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft) #This function and the one below move entities so they appear on the right space in the screen.

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)
    
    def update(self, target, game):  #this little piece of code centers the camera on the player, except when you're at the edge of the map.
        x = -target.rect.centerx + int(game.GAME_W/2)
        y = -target.rect.centery + int(game.GAME_H/2)
        
        x = min(0,x)
        y = min(0,y)
        x = max(-(self.width - game.GAME_W), x)
        y = max(-(self.height - game.GAME_H), y)
        
        self.camera = pg.Rect(x,y,self.width, self.height)
               
