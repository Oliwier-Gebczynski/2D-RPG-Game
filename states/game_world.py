import pygame, os
from states.state import State

class GameWorld(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.current_player = game.current_player
        self.player = Player(self.game)
        self.grass_img = pygame.image.load(os.path.join(self.game.assets_dir, "gfx", "test_bg.jpg"))
        self.font = pygame.font.Font(None, 40)
        self.tree_img = pygame.image.load(os.path.join(self.game.assets_dir, "gfx", "tree.jpeg"))

        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        ]

    def update(self, delta_time, actions):
        if actions["start"]:
            pass
        self.player.update(delta_time, actions, self.map)

    def render(self, display, input_text):
        display.blit(self.grass_img, (0, 0))

        # Render trees
        tile_size = self.game.GAME_W // 20
        self.tree_img = pygame.transform.scale(self.tree_img, (tile_size, tile_size))
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 1:
                    display.blit(self.tree_img, (x * tile_size, y * tile_size))

        #player name
        text_surface = self.font.render(self.current_player, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center= (self.game.GAME_W * 0.1, self.game.GAME_H * 0.1))
        display.blit(text_surface, text_rect)

        self.player.render(display)


class Player():
    def __init__(self, game):
        self.game = game
        self.load_sprites()
        self.position_x, self.position_y = 200, 200
        self.current_frame, self.last_frame_update = 0, 0

    def update(self, delta_time, actions, game_map):
        direction_x = actions["right"] - actions["left"]
        direction_y = actions["down"] - actions["up"]

        new_position_x = self.position_x + 100 * delta_time * direction_x
        new_position_y = self.position_y + 100 * delta_time * direction_y

        # Check window boundaries
        if 0 <= new_position_x <= self.game.GAME_W - self.curr_image.get_width() and 0 <= new_position_y <= self.game.GAME_H - self.curr_image.get_height():
            # Check map collision
            if not self.check_collision(new_position_x, new_position_y, game_map):
                self.position_x, self.position_y = new_position_x, new_position_y

        self.animate(delta_time, direction_x, direction_y)

    def render(self, display):
        display.blit(self.curr_image, (self.position_x, self.position_y))

    def animate(self, delta_time, direction_x, direction_y):
        self.last_frame_update += delta_time

        if not (direction_x or direction_y):
            self.curr_image = self.curr_anim_list[0]
            return

        if direction_x:
            if direction_x > 0:
                self.curr_anim_list = self.right_sprites
            else:
                self.curr_anim_list = self.left_sprites
        if direction_y:
            if direction_y > 0:
                self.curr_anim_list = self.front_sprites
            else:
                self.curr_anim_list = self.back_sprites

        if self.last_frame_update > .15:
            self.last_frame_update = 0
            self.current_frame = (self.current_frame + 1) % len(self.curr_anim_list)
            self.curr_image = self.curr_anim_list[self.current_frame]

    def load_sprites(self):
        self.sprite_dir = os.path.join(self.game.sprite_dir, "player")
        self.front_sprites, self.back_sprites, self.right_sprites, self.left_sprites = [], [], [], []

        for i in range(1, 5):
            self.front_sprites.append(
                pygame.image.load(os.path.join(self.sprite_dir, "player_front" + str(i) + ".png")))
            self.back_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_back" + str(i) + ".png")))
            self.right_sprites.append(
                pygame.image.load(os.path.join(self.sprite_dir, "player_right" + str(i) + ".png")))
            self.left_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_left" + str(i) + ".png")))

        self.curr_image = self.front_sprites[0]
        self.curr_anim_list = self.front_sprites

    def check_collision(self, new_x, new_y, game_map):
        tile_size = self.game.GAME_W // 20
        tile_x = int(new_x // tile_size)
        tile_y = int(new_y // tile_size)

        if game_map[tile_y][tile_x] == 1:
            return True
        return False
