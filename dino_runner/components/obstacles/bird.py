import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

#from dino_runner.utils.constants import RUNNING

class Bird (Obstacle):
   
   Y_POS = 125
   X_POS = 180

   def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = random.randrange(200, 300)
        self.fly_index = 0

   def update(self, game_speed, player):
        self.fly()
        if self.fly_index >= 10:
            self.fly_index = 0
        return super().update(game_speed + 5, player)
     
   def fly(self):
      #print(self.fly_index)
      self.image = BIRD[0] if self.fly_index < 5 else BIRD[1]
      self.fly_index += 1