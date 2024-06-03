import pygame, time
from states.state import State
from states.title import StartMenu

class IntroScreen(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.font = pygame.font.Font(None, 24)  # Adjust font size as needed
        self.start_time = time.time()

    def update(self, delta_time, actions):
        self.game.reset_keys()

    def render(self, display, input_text):
        display.fill((0, 0, 0))

        controls_text = [
            "Controls:",
            "Move Right: Right Arrow",
            "Move Left: Left Arrow",
            "Start: Enter"
        ]

        for i, text in enumerate(controls_text):
            text_surface = self.font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.game.GAME_W * 0.5, self.game.GAME_H * 0.2 + i * 30))
            display.blit(text_surface, text_rect)

    def transition_state(self):
        current_time = time.time()
        if current_time - self.start_time > 10:  # Check if 10 seconds have passed
            new_state = StartMenu(self.game)
            new_state.enter_state()
