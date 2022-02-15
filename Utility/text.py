from states.state import State
import pygame as pg
from pygame import Vector2



class Text():
    def __init__(
        self, 
        font,
        text :str,
        max_width:int, # for wordwrap 
        text_colour = (255,255,255),
        heading = None,
        heading_colour = (255,255,255),
        heading_bg_colour = (0,0,0),
        bg_colour = None,
        antialias = False,    
    ):
        self.text = text
        self.font = font
        self.colour = text_colour
        self.bg_colour = bg_colour
        self.max_width = max_width
        self.heading = heading
        self.head_colour = heading_colour
        self.h_bg_colour = heading_bg_colour
        self.render(antialias)
    
    def render(self, antialias):
        text_surface = self.word_wrap(self.text, self.colour, self.max_width, self.bg_colour, antialias)
        if self.heading != None:
            heading_surface = self.word_wrap(self.heading, self.head_colour, self.max_width, self.h_bg_colour, antialias) 
            self.surface = pg.Surface((text_surface.get_rect().w,text_surface.get_rect().h + heading_surface.get_rect().h),  pg.SRCALPHA)
            self.surface.fill(self.h_bg_colour)
            self.surface.blit(heading_surface, (text_surface.get_rect().w/2 - heading_surface.get_rect().w/2,0))
            self.surface.blit(text_surface, (0, heading_surface.get_rect().h))
        else: 
            self.surface = pg.Surface((text_surface.get_rect().w,text_surface.get_rect().h), pg.SRCALPHA)
            self.surface.blit(text_surface, (0,0))
        self.image = self.surface
        


    def word_wrap(self, text,colour, max_width,bg_colour, antialias):
        words = text.split() #splits into words
        if len(text) >= 1:
            if text[-1] == ' ':  
                words.append(' ')
        if len(words) < 1: font_height = 1
        lines = []
        surf_width = 0
        while len(words) > 0: #this is to get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                font_width, font_height = self.font.size(' '.join(line_words + words[:1])) #checks to see if the next iteration will be too wide, if so it breaks.
                if font_width > max_width:
                    break
                if font_width > surf_width: surf_width = font_width #sets the final 
            #add a line consisting of those words. 
            line = ' '.join(line_words)
            line += ' '
            lines.append(line)
        
            
        #now that we've split the text into lines we need to render them.
        surface = pg.Surface((surf_width, font_height * len(lines)), pg.SRCALPHA) #gotta create the surface first
        if bg_colour != None: surface.fill(bg_colour)
            
        #we'll render each line below the last, so we need to keep track of 
        # the cumulative height of the lines
        y_offset = 0
        for line in lines:
            font_width, font_height = self.font.size(line)
            tx = 0  # (tx, ty) is the top-left of the font surface
            ty = 0 + y_offset
            font_surface = self.font.render(line, antialias, colour)
            surface.blit(font_surface, (tx,ty))
            y_offset += font_height
        return surface

class InputBox():
    def __init__(self, pos, font, forbiddenkeys, game, size, maxchars = 999,
                 ACTIVECOLOR = (255,255,255), INACTIVECOLOR = (100,100,100), RECTCOLOR = (76,80,82), BOXCOLOR = (33,40,45)):
        self.text = ''
        self.value = None 
        self.maxchars = maxchars
        self.flicker = False
        self.frameupdate = 0
        
        self.game = game
        self.game.reset_keys()
        self.game.text = ''
        
        self.size = size
        self.font = font
        self.forbiddenkeys = forbiddenkeys
        self.rect = pg.Rect(pos, self.size)
        
       
        self.RECTCOLOR = RECTCOLOR
        self.BOXCOLOR = BOXCOLOR
        self.color = ACTIVECOLOR
        self.text_image = Text(self.font, self.text, size[0], self.color).image
        #self.image = pg.Surface(size)
        pg.key.start_text_input()
        
    def update(self, max_height, actions, dt):
        
        self.frameupdate += dt
        if self.frameupdate > 0.15: 
            self.frameupdate = 0 
            self.flicker = not self.flicker
            
        if actions["backspace"]:
            self.text = self.text[:-1]
            self.text_image = Text(self.font, self.text, self.size[0], self.color).image
            self.game.reset_keys()
            
        if actions["start"]:
            self.value = self.text
            self.text = ''
            self.text_image = Text(self.font, self.text, self.size[0], self.color).image
            pg.key.stop_text_input()
            self.game.reset_keys()
            
        if len(self.game.text) < self.maxchars and len(self.game.text) >= 1:
                self.text += self.game.text
                self.game.text = ''
                self.game.reset_keys()
                temp_image = Text(self.font, self.text, self.size[0], self.color).image
                if temp_image.get_height() < max_height: self.text_image = temp_image
                
        self.rect.height = max(self.size[1], self.text_image.get_height())         
    
    def render(self, display):
        text_surf = pg.Surface((self.rect.w, self.rect.h), pg.SRCALPHA)
        text_surf.fill(self.BOXCOLOR)
        text_surf.blit(self.text_image, (4,4))
        if self.flicker: pg.draw.rect(text_surf, (255,255,255), [Vector2(self.text_image.get_rect().bottomright) - Vector2(-2,10), (2,10) ])
        pg.draw.rect(text_surf, self.RECTCOLOR, [0,0,self.rect.w, self.rect.h], 2)
        display.blit(text_surf, (self.rect))
    
    def restart(self):
        pg.key.start_text_input()
        self.text = ''
        self.value = None
        self.rect.height = self.size[1] 
        