import pygame
from pygame.time import Clock 
from pytmx.util_pygame import load_pygame
from pygame.locals import *
import pytmx
import sys


#time to create a quick test map. 
running = True
TILESIZE = 16
pygame.display
mainClock = pygame.time.Clock()
pygame.init()
flags = pygame.DOUBLEBUF
pygame.font.init()
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
windowSize = (160,160)
WIDTH = 160
HEIGHT = 160
xoffset = 1
yoffset = 1
screen = pygame.display.set_mode(windowSize, flags, 32)
pygame.display.set_caption("Arkanoid")
#ok so the main idea here
tileDict = {
    "0":"grass",
    "1":"dirt",
    "2":"barrier",
    "P":"player",
    "3":"none"
}

#Reads the map files into a slightly nicer format :)
def generateMap(textfile):
    maplist =[]
    with open(textfile) as f:
        content = f.readlines()
    maplist = [x.strip() for x in content]
    return maplist

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, imagepath):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagepath).convert_alpha()
        self.rect=self.image.get_rect()
        self.x = x
        self.y = y
    def update(self):
        self.rect.x= self.x *TILESIZE   #multiply the x and y by tilesize to draw on screen
        self.rect.y= self.y *TILESIZE

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        
        self.x=x
        self.y=y
    def move(self, x_offset, y_offset, walls_list):  #take in walls list, iterate through to check if a wall occup
        #ies the next location. Make flag moving false if so so no movement possible.
        
        moving = True
        
        for wall in walls_list:
            if wall.x==self.x+x_offset and wall.y==self.y+y_offset:
                moving=False
        if moving:
            self.x+=x_offset
            self.y+=y_offset
          
    def update(self):
        self.rect.x=self.x*TILESIZE   #multiply the x and y by tilesize to draw on screen
        self.rect.y=self.y*TILESIZE
class Camera:
    def __init__(self, width, height):
        self.camera=pygame.Rect(0,0, width, height)
        self.width=width
        self.height=height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)
        x=min(0,x) #stops going off on left
        y=min(0,y) #stops going off on top
       # x=max(-1024-2080,x)
        x=max(-(2080-1024),x)
        y=max(-(800-HEIGHT),y)
        
        self.camera = pygame.Rect(x, y, self.width, self.height)
        


all_sprites_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()


map_data = generateMap("map.txt")
for row, tiles in enumerate(map_data):
    for col, tile in enumerate(tiles):
        if tile != 'P':
            imagepath = "Assets/{}.png".format(tileDict[tile])
            newtile = Tile(row, col, imagepath)
            all_sprites_list.add(newtile)
            if tile == '2':
                wall_list.add(newtile)
        elif tile == 'P':
            player = Player(row,col)
all_sprites_list.add(player)
            
camera = Camera(1,1)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[K_x]:
        running = False
    if keys[K_LEFT]: player.move(-xoffset,0, wall_list)
    if keys[K_RIGHT]: player.move(xoffset,0,wall_list)
    if keys[K_UP]: player.move(0, -yoffset, wall_list )
    if keys[K_DOWN]: player.move(0, yoffset, wall_list)
    
    screen.fill(BLACK)
    all_sprites_list.update()
    camera.update(player)
    #all_sprites_list.draw(screen)
    for sprite in all_sprites_list:
        screen.blit(sprite.image, camera.apply(sprite))
    #all_sprites_list.draw(screen)
    #print("player position is tile " + str((player.rect.x/TILESIZE)+1))
    pygame.display.flip()
    mainClock.tick(60)
# for sprite in wall_list:
    #print(sprite.rect.x)
pygame.quit()