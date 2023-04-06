import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.banana import Banana

class ObstacleManager:

    isBird = False
    isCactus = False
    isBanana = False

    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player):
       
        selection = random.randrange(0,3)

        if (len(self.obstacles)==0):
            if selection == 0:
                self.obstacles.append(Cactus())
                self.isCactus = True
                self.isBird = False
                self.isBanana = False
            elif selection == 1 :
                self.obstacles.append(Bird())
                self.isCactus = False
                self.isBird = True
                self.isBanana = False
            else:
               self.obstacles.append(Banana())
               self.isCactus = False
               self.isBird = False
               self.isBanana = True
        
        for obstacle in self.obstacles:
            if obstacle.isHitHammer:
                self.obstacles.pop()
            elif obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obsacle in self.obstacles:
            obsacle.draw(screen)