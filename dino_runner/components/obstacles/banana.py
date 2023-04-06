import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BANANA

class Banana (Obstacle):
    Y_POS_BANANA = 380

    def __init__(self):
      image = BANANA[0]     
      super().__init__(image)
      self.rect.y = self.Y_POS_BANANA 
       
    