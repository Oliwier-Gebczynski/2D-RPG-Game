#visible_sprites group for sprites that will be drawn 
#ostacle_sprites group for sprites that the player and enemy can collide with

import pygame
from settings import *
from interface import Interface

class GameManager:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.interface = Interface()
    
    def run(self):
        self.interface.run()
        pass

