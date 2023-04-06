import pygame
import random
from dino_runner.utils.constants import SCREEN_WIDTH

class Coin:

    def __init__(self, image):
        self.image = image
       # self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randrange(80, 333)
        self.start_time = 0
        self.time_up = 0
        self.used = False

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if not self.used and self.rect.colliderect(player.dino_rect):
            player.coins += 1
            self.used = True
            print (player.coins)

    def draw (self, screen):
        screen.blit(self.image, self.rect)    