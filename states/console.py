from states.state import State
import pygame as pg
from Utility.text import *
from Utility.util import *
import os

class Console(State):
    def __init__(self, game):
        super().__init__(game)
        self.commandkey = '/'
        
        self.image = pg.image.load(os.path.join("assets", "in-game", "console.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.game.SCREEN_W/2 - 500, self.game.SCREEN_H/2 - 250)
        
        self.font = pg.font.Font(os.path.join("assets", "font", "console.ttf"), 16)
        self.smallfont = pg.font.Font(os.path.join("assets", "font", "console.ttf"), 12)
        self.render_images()
        self.TextBox = InputBox((self.rect.bottomleft), self.font, [], self.game, (1000, 25))
        
    def update(self, delta_time, actions):
        if actions["console"] or actions["return"]:
            self.game.reset_keys()
            self.exit_state()
        
        self.TextBox.update(100, actions, delta_time)
        if self.TextBox.value != None:
            self.game.error_log.append(ConsoleOutput("<{}>".format(self.game.save_data["name"]) + self.TextBox.value))
            self.TextBox.restart()
            self.render_logs()
            #and then right here is where i put the evaluation of the command. i'll do that later.. 
                
    
    def render_images(self):
        height  = 0
        text_images = []
        for log in self.game.error_log:
            text_image = Text(self.smallfont, log, 990).image
            text_images.append(text_image)
            height += text_image.get_height()
        self.text_image = pg.Surface((990,height), pg.SRCALPHA)
        height = 0
        for image in text_images:
            self.text_image.blit(image, (0,height))
            height += image.get_height()        
        self.active_text  = self.text_image.subsurface((0, max(0 , self.text_image.get_height() - 470)), (self.text_image.get_rect().bottomright))
        
    def render_logs(self):
        new_text = Text(self.smallfont, self.game.error_log[-1], 990).image 
        new_surf = pg.Surface((990, self.text_image.get_height() + new_text.get_height()), pg.SRCALPHA)
        new_surf.blit(self.text_image, (0,0))
        new_surf.blit(new_text, (0,self.text_image.get_height()))
        self.text_image = new_surf
        self.active_text  = self.text_image.subsurface((0, max(0 , self.text_image.get_height() - 470)), (self.text_image.get_rect().w, self.text_image.get_rect().h))
    
    def render_text(self, display):
        display.blit(self.image, (self.rect))
        display.blit(self.active_text, (self.rect.x + 5, self.rect.y + 497 - self.active_text.get_height()))
        self.TextBox.render(display)