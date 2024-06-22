import os
import time
import pygame
from states.load import IntroScreen

class Game:
    def __init__(self):
        pygame.init()
        self.GAME_W, self.GAME_H = 512, 512
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1024, 1024
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.running = self.playing = True
        self.actions = self.initialize_actions()
        self.dt = self.prev_time = 0
        self.state_stack = []
        self.input_text = [""]
        self.current_player = ""
        self.load_assets()
        self.load_states()

    def initialize_actions(self):
        return {"left": False, "right": False, "up": False, "down": False, "action1": False, "action2": False, "start": False}

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self.handle_keyup(event)
            elif event.type == pygame.TEXTINPUT:
                self.input_text.append(event.text)

    def handle_keydown(self, event):
        key_action_map = {
            pygame.K_ESCAPE: self.quit_game,
            pygame.K_LEFT: lambda: self.set_action('left', True),
            pygame.K_RIGHT: lambda: self.set_action('right', True),
            pygame.K_UP: lambda: self.set_action('up', True),
            pygame.K_DOWN: lambda: self.set_action('down', True),
            pygame.K_RETURN: lambda: self.set_action('start', True),
            pygame.K_BACKSPACE: lambda: self.input_text.pop() if self.input_text else None,
            pygame.K_s: lambda: self.set_action('action1', True),
            pygame.K_o: lambda: self.set_action('action2', True)
        }
        action = key_action_map.get(event.key)
        if action:
            action()

    def handle_keyup(self, event):
        key_action_map = {
            pygame.K_LEFT: lambda: self.set_action('left', False),
            pygame.K_RIGHT: lambda: self.set_action('right', False),
            pygame.K_UP: lambda: self.set_action('up', False),
            pygame.K_DOWN: lambda: self.set_action('down', False),
            pygame.K_RETURN: lambda: self.set_action('start', False),
            pygame.K_s: lambda: self.set_action('action1', False),
            pygame.K_o: lambda: self.set_action('action2', False)
        }
        action = key_action_map.get(event.key)
        if action:
            action()

    def set_action(self, action, value):
        self.actions[action] = value

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas, self.input_text)
        self.screen.blit(pygame.transform.scale(self.game_canvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0, 0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font = pygame.font.Font(os.path.join(self.font_dir, "PressStart2P-vaV7.ttf"), 20)

    def load_states(self):
        self.title_screen = IntroScreen(self)
        self.state_stack.append(self.title_screen)

    def reset_actions(self):
        for action in self.actions:
            self.actions[action] = False

    # Adding reset_keys for backward compatibility
    def reset_keys(self):
        self.reset_actions()

    def new_save(self):
        split_name = "".join(self.input_text)
        saves_dir = os.path.join("saves")
        if not os.path.exists(saves_dir):
            try:
                os.makedirs(saves_dir)
            except OSError as e:
                print(f"Error creating saves directory: {e}")
                return
        save_path = os.path.join(saves_dir, split_name)

    def quit_game(self):
        self.playing = self.running = False
        pygame.quit()

if __name__ == "__main__":
    game_instance = Game()
    while game_instance.running:
        game_instance.game_loop()
