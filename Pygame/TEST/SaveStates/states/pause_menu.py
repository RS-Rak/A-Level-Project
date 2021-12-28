import pygame, os
from states.state import State

class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)
        