import pygame, sys
from settings import *

class Button:
    def __init__(self, pos, text, text_color, font_size, width=150, height=50, border_width=2, border_color=(0, 0, 0)):
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

class NewSaveView:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
    
    def draw(self, surface):
        font = pygame.font.Font(None, 32)
        start_button = Button((412, 700), "Confirm", (255, 255, 255), font, 200, 50, 2, (255, 255, 255))
        male_button = Button((412, 500), "Male", (255, 255, 255), font, 200, 50, 2, (255, 255, 255))
        female_button = Button((412, 400), "Female", (255, 255, 255), font, 200, 50, 2, (255, 255, 255))

        start_button.draw(self.display_surface)
        male_button.draw(self.display_surface)
        female_button.draw(self.display_surface)

class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('./assets/gfx/test.jpeg')
        FONT = pygame.font.Font(None, 32) 
        self.menu_background = pygame.Surface((412,600)) 
        self.menu_title = TITLE

        self.font = pygame.font.SysFont(None, 24)

        self.new_game = False
        self.second_view = False
    
    def run(self):
        font = pygame.font.Font(None, 32)
        #menu background (photo)
        self.display_surface.blit(self.image, (0, 0))

        #menu background (white)
        
        self.menu_background.set_alpha(192)
        self.menu_background.fill((0,0,0))
        self.display_surface.blit(self.menu_background, (300,200))

        #title
        img = font.render(TITLE, True, (255,255,255))
        self.display_surface.blit(img, (355, 300))

        #display button
        start_button = Button((412, 400), "New Game", (255, 255, 255), font, 200, 50, 2, (255, 255, 255))
        start_button.draw(self.display_surface)

        load_button = Button((412, 500), "Load Game", (255, 255, 255), font, 200, 50, 2, (255, 255, 255))
        load_button.draw(self.display_surface)

        exit_button = Button((412, 600), "Exit", (255, 255, 255), font, 200, 50, 2, (255, 255, 255))
        exit_button.draw(self.display_surface)

        if self.new_game == True:
            self.display_surface.blit(self.image, (0, 0))
            self.display_surface.blit(self.menu_background, (300,200))
            new_save_view = NewSaveView()
            new_save_view.draw(self.display_surface)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.second_view == False:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.check_click(mouse_pos):
                    print("New Game")
                    self.new_game = True
                    self.second_view = True
                elif load_button.check_click(mouse_pos):
                    print("Load Game")
                    self.second_view = True
                elif exit_button.check_click(mouse_pos):
                    pygame.quit()
                    sys.exit()
            


        pygame.display.flip()

        pass