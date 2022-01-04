import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/sprites/player/player_front1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        pass  