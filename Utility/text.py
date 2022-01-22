
import pygame as pg



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
        bg_colour = None          
    ):
        self.text = text
        self.font = font
        self.colour = text_colour
        self.bg_colour = bg_colour
        self.max_width = max_width
        self.heading = heading
        self.head_colour = heading_colour
        self.h_bg_colour = heading_bg_colour
        self.render()
    
    def render(self):
        text_surface = self.word_wrap(self.text, self.colour, self.max_width, self.bg_colour)
        if self.heading != None:
            heading_surface = self.word_wrap(self.heading, self.head_colour, self.max_width, self.bg_colour) 
            self.surface = pg.Surface((text_surface.get_rect().w,text_surface.get_rect().h + heading_surface.get_rect().h))
            self.surface.fill(self.h_bg_colour)
            self.surface.blit(heading_surface, (text_surface.get_rect().w/2 - heading_surface.get_rect().w/2,0))
            self.surface.blit(text_surface, (0, heading_surface.get_rect().h))
        else: 
            self.surface = pg.Surface((text_surface.get_rect().w,text_surface.get_rect().h))
            self.surface.blit(text_surface, (0,0))
        self.image = self.surface
        


    def word_wrap(self, text,colour, max_width,bg_colour):
        words = text.split() #splits into words
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
            lines.append(line)
            
        #now that we've split the text into lines we need to render them. 
        surface = pg.Surface((surf_width, font_height * len(lines) + 10)) #gotta create the surface first
        if bg_colour != None: surface.fill(bg_colour)
        #we'll render each line below the last, so we need to keep track of 
        # the cumulative height of the lines
        y_offset = 0
        for line in lines:
            font_width, font_height = self.font.size(line)
            tx = 0  # (tx, ty) is the top-left of the font surface
            ty = 0 + y_offset
            font_surface = self.font.render(line, True, colour)
            surface.blit(font_surface, (tx,ty))
            y_offset += font_height
        return surface