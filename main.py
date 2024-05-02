import pygame, sys
from settings import *
from game_manager import GameManager

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.get_surface()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.title = pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.intro_counter = 0
        self.title_text_bg = pygame.Surface((824,150))

        self.game_manager = GameManager()
        self.game_started = False
        self.title_bg = pygame.image.load('./assets/gfx/title_bg.jpeg')
        

    def run(self):
        font = pygame.font.Font(None, 64)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            if self.intro_counter == 240:
                self.game_started = True

            if self.game_started:
                self.game_manager.run()

        
            pygame.display.update()

            self.screen.blit(self.title_bg, (0, 0))

            self.title_text_bg.set_alpha(192)
            self.title_text_bg.fill((0,0,0))
            self.screen.blit(self.title_text_bg, (100,250))

            img = font.render(TITLE, True, (255,255,255))
            self.screen.blit(img, (200, 300))

            self.clock.tick(FPS)

            self.intro_counter += 1

if __name__ == '__main__':
    game = Game()
    game.run() 