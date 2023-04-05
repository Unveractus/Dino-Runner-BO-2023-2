import pygame
import random
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import SCREEN_WIDTH

class Cloud:
    def __init__(self):
        self.XPOS = random.randint(1100, 1200)
        self.YPOS = random.randint(50, 50) 
        self.XPOS1 = random.randint(1300, 1500) 
        self.YPOS2 = random.randint(80, 150)
        self.image = CLOUD
        self.image_width = self.image.get_width()
        self.speed = 20

    def update(self):
        self.XPOS -= self.speed
        if self.XPOS < -self.image_width:
            self.XPOS = SCREEN_WIDTH + self.image_width
            self.YPOS = random.randint (100, 90)

    def draw(self, screen):
        screen.blit(self.image,(self.XPOS, self.YPOS))
        