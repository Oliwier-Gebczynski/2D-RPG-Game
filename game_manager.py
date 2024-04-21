#visible_sprites group for sprites that will be drawn 
#ostacle_sprites group for sprites that the player and enemy can collide with

import pygame
from settings import *

class GameManager:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.image = pygame.image.load('./assets/gfx/test.jpeg')
        self.image_rect = self.image.get_rect()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
    
    def run(self):
        self.display_surface.blit(self.image, (0, 0))
        pass

