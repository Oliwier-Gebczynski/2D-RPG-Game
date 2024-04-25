import pygame, sys
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



        self.arrow_down_active = pygame.image.load('./assets/gfx/arrow_active.png')
        self.arrow_up_active = pygame.image.load('./assets/gfx/arrow_active.png')
        self.arrow_left_active = pygame.image.load('./assets/gfx/arrow_active.png')
        self.arrow_right_active = pygame.image.load('./assets/gfx/arrow_active.png')

        self.arrow_down_active = pygame.transform.scale(self.arrow_down, ARROW_SIZE)
        self.arrow_up_active = pygame.transform.scale(self.arrow_up, ARROW_SIZE)
        self.arrow_left_active = pygame.transform.scale(self.arrow_left, ARROW_SIZE)
        self.arrow_right_active = pygame.transform.scale(self.arrow_right, ARROW_SIZE)

        self.arrow_up_active = pygame.transform.rotate(self.arrow_up, 180)
        self.arrow_left_active = pygame.transform.rotate(self.arrow_left, 270)
        self.arrow_right_active = pygame.transform.rotate(self.arrow_right, 90)

    
    def run(self):
        #self.display_surface.blit(self.image, (0, 0))
        white_surface = pygame.Surface((self.display_surface.get_width(), self.display_surface.get_height()))
        white_surface.fill((255, 255, 255)) 
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.display_surface.blit(self.arrow_up_active, UP_ARROW_POS)
                    print("Key UP")
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.display_surface.blit(self.arrow_down_active, DOWN_ARROW_POS)
                    print("Key DOWN")

                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.display_surface.blit(self.arrow_left_active, LEFT_ARROW_POS)
                    print("Key LEFT")

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.display_surface.blit(self.arrow_right_active, RIGHT_ARROW_POS)
                    print("Key RIGHT")
            
            self.display_surface.blit(white_surface, (0, 0))
            self.display_surface.blit(self.arrow_down, DOWN_ARROW_POS)
            self.display_surface.blit(self.arrow_up, UP_ARROW_POS)
            self.display_surface.blit(self.arrow_left, LEFT_ARROW_POS)
            self.display_surface.blit(self.arrow_right, RIGHT_ARROW_POS)
        
        pass

