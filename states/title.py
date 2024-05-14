import pygame, os
from states.state import State

class StartMenu(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)

        # Set the menu font
        self.font = pygame.font.Font(None, 24)  # Adjust font size as needed

        # Set menu options and their positions
        self.menu_options = {"Start": (self.game.GAME_W * 0.2, self.game.GAME_H * 0.6),
                              "Load": (self.game.GAME_W * 0.5, self.game.GAME_H * 0.6),
                              "Exit": (self.game.GAME_W * 0.8, self.game.GAME_H * 0.6)}  # Adjust positions as needed

        # Set initial cursor position (assuming "Start" is selected initially)
        self.selected_index = 0

    def update(self, delta_time, actions):
        if actions["right"]:
            self.selected_index = (self.selected_index + 1) % len(self.menu_options)
        elif actions["left"]:
            self.selected_index = (self.selected_index - 1) % len(self.menu_options)
        if actions["start"]:
            self.transition_state()

        self.game.reset_keys()

    def render(self, display):
        display.fill((0, 0, 0))

        title_surface = self.font.render("Złoty Róg: Skarb Swarożyca", True, (255, 255, 255))  
        title_rect = title_surface.get_rect(center = (self.game.GAME_W * 0.5, self.game.GAME_H * 0.2))
        display.blit(title_surface, title_rect)

        for option, pos in self.menu_options.items():
            text_surface = self.font.render(option, True, (255, 255, 255))  
            text_rect = text_surface.get_rect(center=pos)
            display.blit(text_surface, text_rect)

        if self.selected_index is not None:
            selected_option, selected_pos = list(self.menu_options.items())[self.selected_index]
            text_rect = self.font.render(selected_option, True, (255, 255, 255)).get_rect()  
            line_start_x = selected_pos[0] - 25 
            line_end_x = selected_pos[0] + 25 
            line_y = selected_pos[1] + 10 
            pygame.draw.line(display, (255, 255, 255), (line_start_x, line_y), (line_end_x, line_y), 2)  

    def transition_state(self):
        selected_option = list(self.menu_options.keys())[self.selected_index]
        if selected_option == "Start":
            
            pass
        elif selected_option == "Load":
            
            pass
        elif selected_option == "Exit":
            self.game.quit()  

