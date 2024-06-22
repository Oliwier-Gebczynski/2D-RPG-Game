import random
import math

class Enemy:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.dir_x = 1
        self.dir_y = 1
        self.angle = random.uniform(0, 2 * math.pi)
        self.attack = 0.2
        self.hp = 100

    def update(self, delta_time, game_map, tile_size):
        new_x = self.x + self.speed * math.cos(self.angle) * delta_time
        new_y = self.y + self.speed * math.sin(self.angle) * delta_time

        if new_x < 0 or new_x > len(game_map[0]) * tile_size - self.image.get_width():
            self.angle = random.uniform(0, 2 * math.pi)
        if new_y < 0 or new_y > len(game_map) * tile_size - self.image.get_height():
            self.angle = random.uniform(0, 2 * math.pi)

        tile_x = int(new_x // tile_size)
        tile_y = int(new_y // tile_size)
        if game_map[tile_y][tile_x] == 1:
            self.angle = random.uniform(0, 2 * math.pi)

        self.x += self.speed * math.cos(self.angle) * delta_time
        self.y += self.speed * math.sin(self.angle) * delta_time

    def render(self, display):
        display.blit(self.image, (self.x, self.y))
