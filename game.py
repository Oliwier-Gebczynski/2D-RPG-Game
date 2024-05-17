import os, time, pygame, json
from states.title import StartMenu

class Game():
        def __init__(self):
            pygame.init()
            self.GAME_W,self.GAME_H = 512, 512
            self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 1024, 1024
            self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
            self.running, self.playing = True, True
            self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False}
            self.dt, self.prev_time = 0, 0
            self.state_stack = []
            self.load_assets()
            self.load_states()
            self.input_text = [""]

        def game_loop(self):
            while self.playing:
                self.get_dt()
                self.get_events()
                self.update()
                self.render()

        def get_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                if event.type == pygame.TEXTINPUT:
                    self.input_text += event.text
                    print(self.input_text)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                    if event.key == pygame.K_LEFT:
                        self.actions['left'] = True
                    if event.key == pygame.K_RIGHT:
                        self.actions['right'] = True
                    if event.key == pygame.K_UP:
                        self.actions['up'] = True
                    if event.key == pygame.K_DOWN:
                        self.actions['down'] = True    
                    if event.key == pygame.K_RETURN:
                        self.actions['start'] = True  
                    if event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.actions['left'] = False
                    if event.key == pygame.K_d:
                        self.actions['right'] = False
                    if event.key == pygame.K_w:
                        self.actions['up'] = False
                    if event.key == pygame.K_s:
                        self.actions['down'] = False
                    if event.key == pygame.K_p:
                        self.actions['action1'] = False
                    if event.key == pygame.K_o:
                        self.actions['action2'] = False
                    if event.key == pygame.K_RETURN:
                        self.actions['start'] = False  

        def update(self):
            self.state_stack[-1].update(self.dt,self.actions)

        def render(self):
            self.state_stack[-1].render(self.game_canvas, self.input_text)
            
            self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
            pygame.display.flip()

        def get_dt(self):
            now = time.time()
            self.dt = now - self.prev_time
            self.prev_time = now

        def draw_text(self, surface, text, color, x, y):
            text_surface = self.font.render(text, True, color)
            #text_surface.set_colorkey((0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_surface, text_rect)

        def load_assets(self):
            self.assets_dir = os.path.join("assets")
            self.sprite_dir = os.path.join(self.assets_dir, "sprites")
            self.font_dir = os.path.join(self.assets_dir, "font")
            self.font= pygame.font.Font(os.path.join(self.font_dir, "PressStart2P-vaV7.ttf"), 20)

        def load_states(self):
            self.title_screen = StartMenu(self)
            self.state_stack.append(self.title_screen)

        def reset_keys(self):
            for action in self.actions:
                self.actions[action] = False

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


        def quit(self):
            pygame.quit()
            quit() 

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()