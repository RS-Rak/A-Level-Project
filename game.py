import pygame as pg
import pygame
import os, time

from states.menus import *




class Game():
    def __init__(self):
        pg.init()
        self.GAME_W, self.GAME_H = 400, 224
        self.SCREEN_W, self.SCREEN_H = pg.display.Info().current_w, pg.display.Info().current_h
        self.RATIO_X = self.SCREEN_W/self.GAME_W
        self.RATIO_Y = self.SCREEN_H/self.GAME_H
        self.game_canvas = pg.Surface((self.GAME_W, self.GAME_H))
        self.screen = pg.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        
        self.save_data = None #on launch, save slot is none
        self.save_slot = None
        #Player controlled actions. I'll insert more/change when necessary. 
        self.actions ={
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "interact": False,
            "attack": False,
            "alt-attack":False,
            "start": False,  
            "return":False,
            "inventory": False         
        }
        self.dt, self.prev_time = 0 , 0 #This is for framerate indepence annd delta time.
        self.state_stack =[] #this is a list, but i'm gonna treat it like a stack. 
        self.clock = pg.time.Clock() # clockin
        self.FPS = 200
        self.load_assets()
        self.load_states()
    
    def game_loop(self):
        while self.playing:
            self.dt = self.clock.tick(self.FPS) / 1000 #gets delta_time from the self.clock.tick
            self.get_events()
            self.update()
            self.render()
            
    
        
    def get_events(self):
        #This basically checks what interactions are happening every game loop pretty much. 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running, self.playing = False, False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.actions['return'] = True
                if event.key == pg.K_a:
                    self.actions['left'] = True
                if event.key == pg.K_d:
                    self.actions['right'] = True
                if event.key == pg.K_s:
                    self.actions['down'] = True
                if event.key == pg.K_w:
                    self.actions['up'] = True
                if event.key == pg.K_f:
                    self.actions['interact'] = True
                if event.key == pg.K_RETURN:
                    self.actions['start'] = True
                if event.key == pg.K_TAB:
                    self.actions['inventory'] = True
                    
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions['attack'] = True
                if event.button == 3:
                    self.actions['alt-attack'] = True
                    
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.actions['return'] = False
                if event.key == pg.K_a:
                    self.actions['left'] = False
                if event.key == pg.K_d:
                    self.actions['right'] = False
                if event.key == pg.K_s:
                    self.actions['down'] = False
                if event.key == pg.K_w:
                    self.actions['up'] = False
                if event.key == pg.K_f:
                    self.actions['interact'] = False
                if event.key == pg.K_RETURN:
                    self.actions['start'] = False
                if event.key == pg.K_TAB:
                    self.actions["inventory"] = False
                    
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.actions['attack'] = False
                if event.button == 3:
                    self.actions['alt-attack'] = False
    
    def update(self):
        self.state_stack[-1].update(self.dt, self.actions) #updates whatevers on top of the state stack
    
    def render_text(self): #renders text - text has to be rendered last else it'll blur oddly.
        if len(self.state_stack) > 0:
            self.state_stack[-1].render_text()
        pygame.display.flip()
        
    def render(self):
        #scales up the game canvas to the size of the actual screen
        if len(self.state_stack) > 0:
            self.state_stack[-1].render(self.game_canvas)
            self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_W, self.SCREEN_H)), (0,0))
        else: self.playing, self.running = False, False
        self.render_text()
        pygame.display.flip()
    
    def draw_text(self, surface, text, color, x,y, font): 
        #this is one of my functions for drawing text to the screen. 
        x = x * self.RATIO_X
        y = y * self.RATIO_Y
        text_surface = font.render(text, False, color)
        #text_surface.set_colorkey((0,0,0)) #this is for transparent fonts
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text_surface, text_rect)
    
    def load_assets(self):
        # This creates pointers to directories. 
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")     
        self.button_dir = os.path.join(self.assets_dir, "buttons")
        self.font = pygame.font.Font(os.path.join(self.font_dir, "m6x11.ttf") , 60) 
        self.small_font = pygame.font.Font(os.path.join(self.font_dir, "m6x11.ttf") , 30) 
        self.alt_font = pygame.font.Font(os.path.join(self.font_dir, "pixelfont.ttf") , 144) 
        self.icon_dir = os.path.join(self.assets_dir, "icons")
        self.background_dir = os.path.join(self.assets_dir, "background")
        
    def load_states(self):
        #this puts the main menu as the first thing in the stack because why not
        self.title_screen = Menu(self)
        self.state_stack.append(self.title_screen)
    
    def reset_keys(self):
        #resets any key presses. 
        for action in self.actions:
            self.actions[action] = False

if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()