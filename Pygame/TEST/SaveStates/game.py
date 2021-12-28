import pygame as pg
import pygame
import os, time

from states.menu import Menu




class Game():
    def __init__(self):
        pg.init()
        self.GAME_W, self.GAME_H = 800, 464
        self.SCREEN_W, self.SCREEN_H = 1600, 928
        self.game_canvas = pg.Surface((self.GAME_W, self.GAME_H))
        self.screen = pg.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
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
            "paused":False          
        }
        self.dt, self.prev_time = 0 , 0 #This is for framerate indepence annd delta time.
        self.state_stack =[] #this is a list, but i'm gonna treat it like a stack. 
        self.load_assets()
        self.load_states()
    
    def game_loop(self):
        while self.playing:
            self.get_dt()
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
                    self.actions['paused'] = True
                if event.key == pg.K_a:
                    self.actions['left'] = True
                if event.key == pg.K_d:
                    self.actions['right'] = True
                if event.key == pg.K_s:
                    self.actions['down'] = True
                if event.key == pg.K_w:
                    self.actions['up'] = True
                if event.key == pg.K_e:
                    self.actions['interact'] = True
                if event.key == pg.K_RETURN:
                    self.actions['start'] = True
                    
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions['attack'] = True
                if event.button == 3:
                    self.actions['alt-attack'] = True
                    
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.actions['paused'] = False
                if event.key == pg.K_a:
                    self.actions['left'] = False
                if event.key == pg.K_d:
                    self.actions['right'] = False
                if event.key == pg.K_s:
                    self.actions['down'] = False
                if event.key == pg.K_w:
                    self.actions['up'] = False
                if event.key == pg.K_e:
                    self.actions['interact'] = False
                if event.key == pg.K_RETURN:
                    self.actions['start'] = False
                    
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.actions['attack'] = False
                if event.button == 3:
                    self.actions['alt-attack'] = False
    
    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)
    
    def render(self):
        #scales up the game canvas to the size of the actual screen
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_W, self.SCREEN_H)), (0,0))
        pygame.display.flip()
    
    def get_dt(self):
        #this calculates delta time, the change in time between framerates to ensure framerate independece. 
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
    
    def draw_text(self, surface, text, color, x,y):
        #this is my function for drawing text to the screen. 
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0)) #this is for transparent fonts
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        surface.blit(text_surface, text_rect)
    
    def load_assets(self):
        # This creates pointers to directories. 
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")     
        self.font = pygame.font.Font(os.path.join(self.font_dir, "mainfont.ttf") , 20) 
    
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