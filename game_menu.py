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
        self.active_color = (0, 255, 0)  
        self.is_active = False  
        self.clicked = False  

        FONT = pygame.font.Font(None, font_size) 

        self.text_surface = FONT.render(text, True, text_color)

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height) 

    def draw(self, surface):
        pygame.draw.rect(surface, self.border_color, self.rect, self.border_width)
        surface.blit(self.text_surface, self.text_surface.get_rect(center=self.rect.center))

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos): 
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:  
                self.clicked = True
                return True 
            else:
                self.clicked = False  
        return False 

    def change_active_state(self):
        if self.is_active == False:
            self.border_color = self.active_color
            self.is_active = True
        else:
            self.border_color = (255, 255, 255)
            self.is_active = False

class NewSaveView:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.confirm_button = Button((412, 700), "Confirm", (255, 255, 255), 32, 200, 50, 2, (255, 255, 255))
        self.male_button = Button((412, 500), "Male", (255, 255, 255), 32, 200, 50, 2, (255, 255, 255))
        self.female_button = Button((412, 400), "Female", (255, 255, 255), 32, 200, 50, 2, (255, 255, 255))
    
    def draw(self, surface):
        self.confirm_button.draw(self.display_surface)
        self.male_button.draw(self.display_surface)
        self.female_button.draw(self.display_surface)
    
    def run(self):
        running = True

        while running:
            self.draw(self.display_surface)
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.female_button.check_click(mouse_pos):
                        print("Female")
                        print(self.female_button.is_active)
                        self.female_button.change_active_state() 
                    elif self.male_button.check_click(mouse_pos):
                        print("Male")
                        print(self.male_button.is_active)
                        self.male_button.change_active_state()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

        pygame.display.update()
        self.clock.tick(FPS)

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 24)
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('./assets/gfx/test.jpeg')
        FONT = pygame.font.Font(None, 32) 
        self.menu_background = pygame.Surface((412,600)) 
        self.menu_title = TITLE
        self.img = self.font.render(TITLE, True, (255,255,255))
        self.clock = pygame.time.Clock()

        self.new_game = False
        self.second_view = False

        self.start_button = Button((412, 400), "New Game", (255, 255, 255), 32, 200, 50, 2, (255, 255, 255))
        self.load_button = Button((412, 500), "Load Game", (255, 255, 255), 32, 200, 50, 2, (255, 255, 255))
        self.exit_button = Button((412, 600), "Exit", (255, 255, 255), 32, 200, 50, 2, (255, 255, 255))

        self.new_save_view = NewSaveView()
        
    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()

            #menu background (photo)
            self.display_surface.blit(self.image, (0, 0))

            #menu background (white)
            self.menu_background.set_alpha(192)
            self.menu_background.fill((0,0,0))
            self.display_surface.blit(self.menu_background, (300,200))

            #title
            self.display_surface.blit(self.img, (355, 300))

            #display button zrobic fora do draw 
            for element in self.menu_elements:
                element.draw(self.display_surface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.new_game == False:
                    
                    if self.start_button.check_click(mouse_pos):
                        print("New Game")
                        self.new_save_view.run()
                    elif self.load_button.check_click(mouse_pos):
                        print("Load Game")
                    elif self.exit_button.check_click(mouse_pos):
                        pygame.quit()
                        sys.exit()
        
            pygame.display.update()
            self.clock.tick(FPS)

        pass