import pygame, sys
from settings import *
from game_manager import GameManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.title = pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.game_manager = GameManager()
        self.game_started = False
        self.title_bg = pygame.image.load('./assets/gfx/title_bg.jpeg')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_started = True
            
            if self.game_started:
                self.game_manager.run()

            pygame.display.update()

            self.screen.blit(self.title_bg, (0, 0))
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run() 