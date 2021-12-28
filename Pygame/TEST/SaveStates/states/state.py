#This is an abstract parent for my other states - menu, options, etc. 

class State():
    def __init__(self, game):
        self.game = game
        self.pre_state = None # keeps track of what state is currently below our current state. 
    
    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        #surface here is gonna be the game canvas
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1: #if there's more than one item in the stack, that means we need to keep track of prev. state
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self) #ads it to the state that's wild. 
    
    def exit_state(self):
        self.game.state_stack.pop()