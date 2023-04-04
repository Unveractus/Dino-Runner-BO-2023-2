import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

#from dino_runner.utils.constants import RUNNING

class Bird (Obstacle):
   
   Y_POS = 125
   X_POS = 180

   def __init__(self):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.X_POS
        self.bird_rect.y = self.Y_POS
        self.fly_index = 0
        self.bird_fly = True
        super().__init__(self.image)

     
   def fly(self):
      self.image = BIRD[0] if self.fly_index < 2 else BIRD[1]
      self.bird_rect = self.image.get_rect()
      self.bird_rect.x = self.X_POS
      self.bird_rect.y = self.Y_POS
      self.fly_index += 1