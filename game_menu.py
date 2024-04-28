import pygame, sys
from settings import *

class Button:
    def __init__(self, pos, text, text_color, font_size, width=100, height=50, border_width=2, border_color=(0, 0, 0)):
        self.pos = pos
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.width = width
        self.height = height
        self.border_width = border_width
        self.border_color = border_color
        FONT = pygame.font.Font(None, 32) 

        self.text_surface = FONT.render(text, True, text_color)

        self.text_rect = self.text_surface.get_rect(center=(self.pos[0] + self.width // 2, self.pos[1] + self.height // 2))

    def draw(self, surface):
        pygame.draw.rect(surface, self.border_color,
                         (self.pos[0], self.pos[1], self.width, self.height), self.border_width)
        surface.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_pos):
        button_rect = pygame.Rect(self.pos[0], self.pos[1], self.width + self.border_width * 2, self.height + self.border_width * 2)
        return button_rect.collidepoint(mouse_pos)

class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('./assets/gfx/test.jpeg')
        FONT = pygame.font.Font(None, 32) 
    
    def run(self):
        self.display_surface.blit(self.image, (0, 0))

        font = pygame.font.Font(None, 32)
        start_button = Button((412, 500), "Start Game", (255, 255, 255), font, 150, 50, 2, (255, 255, 255))
        start_button.draw(self.display_surface)
        
        pass