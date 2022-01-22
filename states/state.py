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

    def enter_state(self): #adds a state to the stack. 
        if len(self.game.state_stack) > 1: #if there's more than one item in the stack, that means we need to keep track of prev. state
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self) #ads it to the state that's wild. 
    
    def exit_state(self): #removes a state from the stack
        self.game.state_stack.pop()
    
   