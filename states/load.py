import pygame, time
from states.state import State
from states.title import StartMenu

class IntroScreen(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.font = pygame.font.Font(None, 24) 
        self.view_time = 0
    def update(self, delta_time, actions):
        self.game.reset_keys()
        self.view_time += 1

        if self.view_time == 1000:
            self.transition_state()

    def render(self, display, input_text):
        display.fill((0, 0, 0))

        controls_text = [
            "Controls:",
            "Move Up: Up Arrow",
            "Move Down: Down Arrow",
            "Move Right: Right Arrow",
            "Move Left: Left Arrow",
            "Start: Enter"
        ]

        title_surface = self.font.render("Złoty Róg: Skarb Swarożyca", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center = (self.game.GAME_W * 0.5, self.game.GAME_H * 0.2))
        display.blit(title_surface, title_rect)

        for i, text in enumerate(controls_text):
            text_surface = self.font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.game.GAME_W * 0.5, self.game.GAME_H * 0.4 + i * 30))
            display.blit(text_surface, text_rect)

    def transition_state(self):
        new_state = StartMenu(self.game)
        new_state.enter_state()
