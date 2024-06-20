import pygame, os, random, item
from states.state import State

class GameWorld(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.current_player = game.current_player
        self.player = Player(self.game)
        self.font = pygame.font.Font(None, 40)
        self.small_font = pygame.font.Font(None, 15)
        self.tree_img = pygame.image.load(os.path.join(self.game.assets_dir, "gfx", "tree.png"))
        self.priest_img = pygame.image.load(os.path.join(self.game.assets_dir, "gfx", "priest.png"))
        self.chest_closed = pygame.image.load(os.path.join(self.game.assets_dir, "gfx", "ChestClosed.png"))
        self.chest_open = pygame.image.load(os.path.join(self.game.assets_dir, "gfx", "ChestOpen.png"))
        self.tile_size = self.game.GAME_W // 20
        self.display_hint = False

        self.bar_width = 150
        self.bar_height = 20
        self.bar_margin = 10

        # Create bar objects using player properties
        self.hp_bar = Bar(350, 400, self.bar_width, self.bar_height, (255, 0, 0), "HP")
        self.stamina_bar = Bar(350, 400 + 2*self.bar_margin, self.bar_width, self.bar_height, (0, 255, 0), "Stamina")
        self.level_bar = Bar(350, 400 + 4*self.bar_margin, self.bar_width, self.bar_height, (0, 0, 255), "LVL")

        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [5, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        ]

    def update(self, delta_time, actions):
        direction_x = actions["right"] - actions["left"]
        direction_y = actions["down"] - actions["up"]

        if actions["start"]:
            pass
        self.player.update(delta_time, actions, self.map)
        self.detect_collision(delta_time, direction_x, direction_y, self.map)

        self.hp_bar.update(self.player.get_hp(), self.player.get_max_hp())
        self.stamina_bar.update(self.player.get_stamina(), self.player.get_max_stamina())
        self.level_bar.update(self.player.get_level(), self.player.get_max_level())

    def render(self, display, input_text):
        display.fill((0, 0, 0))

        # Render trees
        self.tree_img = pygame.transform.scale(self.tree_img, (self.tile_size, self.tile_size))
        self.chest_closed = pygame.transform.scale(self.chest_closed, (self.tile_size, self.tile_size))
        self.chest_open = pygame.transform.scale(self.chest_open, (self.tile_size, self.tile_size))
        self.priest_img = pygame.transform.scale(self.priest_img, (self.tile_size, self.tile_size))
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 1:
                    display.blit(self.tree_img, (x * self.tile_size, y * self.tile_size))
                if tile == 2:
                    display.blit(self.chest_closed, (x * self.tile_size, y * self.tile_size))
                if tile == 3:
                    display.blit(self.chest_open, (x * self.tile_size, y * self.tile_size))
                if tile == 4:
                    display.blit(self.priest_img, (x * self.tile_size, y * self.tile_size))

        #player name
        text_surface = self.font.render(self.current_player, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center= (self.game.GAME_W * 0.1, self.game.GAME_H * 0.1))
        display.blit(text_surface, text_rect)

        #player items
        offset = 0
        for item in self.player.items:
            text_surface = self.small_font.render(item.name, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center= (self.game.GAME_W * 0.9, self.game.GAME_H * 0.1 + offset))
            display.blit(text_surface, text_rect)
            offset += 20

        if self.display_hint == True:
            black_background = pygame.Surface((self.game.GAME_W, self.game.GAME_H * 0.6)) # Adjust width and height as needed
            black_background.fill((0, 0, 0))

            controls_text = [
                "Greetings, traveler. I sense trouble in your heart. What brings you to our humble village?",
                "The villagers are plagued by monsters from the woods.",
                "Defeat these beasts and you'll earn reward and gratitude.",
                "Beware, for they are strong and cunning.",
                "I believe in your strength and the divine power that guides you.",
                "Go forth and vanquish the evil that plagues our land. Good luck!",
            ]

            for i, text in enumerate(controls_text):
                text_surface = self.small_font.render(text, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(black_background.get_width() * 0.5, 15 + i * 30))
                black_background.blit(text_surface, text_rect)
                display.blit(black_background, (0, self.game.GAME_H * 0.2))

        self.player.render(display)

        # display bars
        self.hp_bar.draw(display, self.player.get_max_hp())
        self.stamina_bar.draw(display, self.player.get_max_stamina())
        self.level_bar.draw(display, self.player.get_max_level())

    def detect_collision(self, delta_time, direction_x, direction_y, game_map):
        player_position_x, player_position_y = self.player.get_position()

        new_position_x = player_position_x + 100 * delta_time * direction_x
        new_position_y = player_position_y + 100 * delta_time * direction_y

        # Check window boundaries
        if 0 <= new_position_x <= self.game.GAME_W - self.player.curr_image.get_width() and 0 <= new_position_y <= self.game.GAME_H - self.player.curr_image.get_height():
            # Check map collision
            if not self.check_collision(new_position_x, new_position_y, game_map):
                self.player.position_x, self.player.position_y = new_position_x, new_position_y

            if self.check_special_tile_collision(new_position_x, new_position_y, game_map, tile_type=0):
                self.display_hint = False

            if self.check_special_tile_collision(new_position_x, new_position_y, game_map, tile_type=2):
                self.player.items.append(self.get_random_item())
                game_map[int(new_position_y // self.tile_size)][int(new_position_x // self.tile_size)] = 3
                #print("Chest opened!")

            if self.check_special_tile_collision(new_position_x, new_position_y, game_map, tile_type=4):
                self.display_hint = True

            if self.check_special_tile_collision(new_position_x, new_position_y, game_map, tile_type=5):
                self.player.hp -= 1
                #print("Hint tile found!")

            #self.display_hint = False

    def check_collision(self, new_x, new_y, game_map):

        tile_x = int(new_x // self.tile_size)
        tile_y = int(new_y // self.tile_size)

        if game_map[tile_y][tile_x] == 1:
            return True
        return False

    def check_special_tile_collision(self, new_x, new_y, game_map, tile_type):
        tile_size = self.game.GAME_W // 20
        tile_x = int(new_x // tile_size)
        tile_y = int(new_y // tile_size)

        if game_map[tile_y][tile_x] == tile_type:
            return True
        return False

    def get_random_item(self):
        items = [#item.Sword("Longsword of Doom", "A magnificent sword with great attack power.", 20),
                 item.Armor("Dragon Armor", "Heavy armor providing excellent protection.", 50),
                 item.GoldenApple("Golden Apple", "A legendary fruit with magical stamina increase.", 100)]
        return random.choice(items)

class Player():
    def __init__(self, game):
        self.game = game
        self.load_sprites()
        self.position_x, self.position_y = 0, 0
        self.current_frame, self.last_frame_update = 0, 0
        self.items = []
        self.item_iterator = 0

        self.hp = 100
        self.max_hp = 100

        self.stamina = 100
        self.max_stamina = 100

        self.attack = 10

        self.max_lvl = 100
        self.lvl = 1

    def update(self, delta_time, actions, game_map):
        direction_x = actions["right"] - actions["left"]
        direction_y = actions["down"] - actions["up"]

        self.animate(delta_time, direction_x, direction_y)
        self.item_action()

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

    def item_action(self):
        if self.item_iterator != len(self.items):
            last_item = self.items[-1]

            if last_item.name == "Longsword of Doom":
                self.attack += last_item.attack
                print("Sword")
            elif last_item.name == "Dragon Armor":
                self.hp += last_item.defense
                self.max_hp += last_item.defense
                print("Armor")
            elif last_item.name == "Golden Apple":
                self.stamina += last_item.healing_power
                self.max_stamina += last_item.healing_power
                print("Apple")

            self.item_iterator += 1

    def get_position(self):
        return self.position_x, self.position_y

    def get_hp(self):
        return self.hp

    def get_stamina(self):
        return self.stamina

    def get_level(self):
        return self.lvl

    def get_max_hp(self):
        return self.max_hp

    def get_max_stamina(self):
        return self.max_stamina

    def get_max_level(self):
        return self.max_lvl

class Bar:
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.value = 0

    def draw(self, screen, max_points):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

        fill_percent = min(self.value / max_points, 1)

        fill_height = int(fill_percent * self.height)

        pygame.draw.rect(screen, self.color, (self.x, self.y + self.height - fill_height, self.width, fill_height))

        font = pygame.font.Font(None, 16)
        text_surface = font.render(f"{self.text}: {self.value}/{max_points}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def update(self, value, max_points):
        self.value = max(0, min(value, max_points))