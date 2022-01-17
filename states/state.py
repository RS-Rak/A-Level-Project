#This is an abstract parent for my other states - menu, options, etc.
import pygame as pg 

class State():
    def __init__(self, game):
        self.game = game
        self.pre_state = None # keeps track of what state is currently below our current state. 
    
    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        #surface here is gonna be the game canvas
        pass
    
    def render_text(self):
        pass
    
    def render_list(self, imagelist, display): #renders every image in a list
        for i in range(len(imagelist)):
            display.blit(imagelist[i].image, (imagelist[i].rect))
    
    def render_dict(self, imagedict, display): #same as above but for dicts
        for i in imagedict:
            display.blit(imagedict[i].image, (imagedict[i].rect))
            
    def word_wrap(self,text, font, colour, x, y, allowed_width): #this is my word-wrap function - it helps keep the text nice and neat.
        words = text.split() #splits into words
        lines = []
        
        while len(words) > 0: #this is to get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                font_width, font_height = font.size(' '.join(line_words + words[:1])) #checks to see if the next iteration will be too wide, if so it breaks.
                if font_width > allowed_width:
                    break
            
            #add a line consisting of those words. 
            line = ' '.join(line_words)
            lines.append(line)
            
        #now that we've split the text into lines we need to render them. 
        surface = pg.Surface((allowed_width, font_height * len(lines) + 10)) #gotta create the surface first
        #we'll render each line below the last, so we need to keep track of 
        # the cumulative height of the lines
        y_offset = 0
        for line in lines:
            font_width, font_height = font.size(line)
            
            # (tx, ty) is the top-left of the font surface
            tx = x 
            ty = y + y_offset
            
            font_surface = font.render(line, True, colour)
            surface.blit(font_surface, (tx,ty))
            
            y_offset += font_height
        return surface
        

    def enter_state(self): #adds a state to the stack. 
        if len(self.game.state_stack) > 1: #if there's more than one item in the stack, that means we need to keep track of prev. state
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self) #ads it to the state that's wild. 
    
    def exit_state(self): #removes a state from the stack
        self.game.state_stack.pop()
    
   