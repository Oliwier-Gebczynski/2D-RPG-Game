import pygame, sys
from settings import *

class Interface:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('./assets/gfx/test.jpeg')

    
    def run(self):
        self.display_surface.blit(self.image, (0, 0))

        pass