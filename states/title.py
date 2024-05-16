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

    def render(self, display, input_text):
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
            new_state = NewGame(self.game)
            new_state.enter_state()
        elif selected_option == "Load":
            
            pass
        elif selected_option == "Exit":
            self.game.quit()  

class NewGame(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)

        # Set the menu font
        self.font = pygame.font.Font(None, 24)  # Adjust font size as needed

        # Set menu options and their positions
        self.menu_options = {"Confirm": (self.game.GAME_W * 0.4, self.game.GAME_H * 0.8),
                             "Back": (self.game.GAME_W * 0.6, self.game.GAME_H * 0.8)}  # Adjust positions as needed

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

    def render(self, display, input_text):
        display.fill((0, 0, 0))

        title_surface = self.font.render("Złoty Róg: Skarb Swarożyca", True, (255, 255, 255))  
        title_rect = title_surface.get_rect(center = (self.game.GAME_W * 0.5, self.game.GAME_H * 0.2))
        display.blit(title_surface, title_rect)

        enter_surface = self.font.render("Enter name", True, (255, 255, 255))  
        enter_rect = enter_surface.get_rect(center = (self.game.GAME_W * 0.5, self.game.GAME_H * 0.4))
        display.blit(enter_surface, enter_rect)

        self.draw_text(input_text, self.font, (255, 255, 255), self.game.GAME_W * 0.5, self.game.GAME_H * 0.5, display)

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
        if selected_option == "Confirm":
            pass
        elif selected_option == "Back":
            while len(self.game.state_stack) > 1:
                self.game.state_stack.pop()

    def draw_text(self, text, font, text_col, x, y, display):
        text_to_display = "".join(text)  # Concatenate all letters into a single string
        img = font.render(text_to_display, True, text_col)  # Render the entire string
        width = img.get_width()  # Get the width of the rendered text
        display.blit(img, (x - (width / 2), y))


