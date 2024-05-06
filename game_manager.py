#visible_sprites group for sprites that will be drawn 
#ostacle_sprites group for sprites that the player and enemy can collide with

import pygame
from settings import *
from interface import Interface
from game_menu import Menu

class GameManager:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.interface = Interface()
        self.game_menu = Menu()
    
    def run(self):
        #self.interface.run()
        while True:
            self.game_menu.run()
        
        pass

