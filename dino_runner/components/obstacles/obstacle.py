import pygame
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.isHitHammer = False

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if not self.isHitHammer: 
         if self.rect.colliderect(player.dino_rect):
             if not self.isHitHammer and player.hammer:
              self.isHitHammer = True
              player.reset()
             elif not player.shield:
              pygame.time.delay(300)
              player.dino_dead = True
             

    def draw(self, screen):
        screen.blit(self.image, self.rect)