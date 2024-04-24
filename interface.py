import pygame
from settings import *

class Interface:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.image = pygame.image.load('./assets/gfx/test.jpeg')
        self.arrow_down = pygame.image.load('./assets/gfx/arrow.png')
        self.arrow_up = pygame.image.load('./assets/gfx/arrow.png')
        self.arrow_left = pygame.image.load('./assets/gfx/arrow.png')
        self.arrow_right = pygame.image.load('./assets/gfx/arrow.png')

        self.arrow_down = pygame.transform.scale(self.arrow_down, ARROW_SIZE)
        self.arrow_up = pygame.transform.scale(self.arrow_up, ARROW_SIZE)
        self.arrow_left = pygame.transform.scale(self.arrow_left, ARROW_SIZE)
        self.arrow_right = pygame.transform.scale(self.arrow_right, ARROW_SIZE)

        self.arrow_up = pygame.transform.rotate(self.arrow_up, 180)
        self.arrow_left = pygame.transform.rotate(self.arrow_left, 270)
        self.arrow_right = pygame.transform.rotate(self.arrow_right, 90)
    
    def run(self):
        #self.display_surface.blit(self.image, (0, 0))
        white_surface = pygame.Surface((self.display_surface.get_width(), self.display_surface.get_height()))
        
        white_surface.fill((255, 255, 255)) 
        self.display_surface.blit(white_surface, (0, 0))

        self.display_surface.blit(self.arrow_down, DOWN_ARROW_POS)
        self.display_surface.blit(self.arrow_up, UP_ARROW_POS)
        self.display_surface.blit(self.arrow_left, LEFT_ARROW_POS)
        self.display_surface.blit(self.arrow_right, RIGHT_ARROW_POS)
        pass

