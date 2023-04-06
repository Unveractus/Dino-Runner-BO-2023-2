import random
from dino_runner.components.coins.gold_coin import GoldCoin 
#from dino_runner.components.power_ups.hammer import Hammer

class CoinManager:
   def __init__(self):
    self.coins = []
       

   def update(self, game_speed, points, player):
      
      if len(self.coins) == 0 and points % 5 == 0:
         selection = random.randint(0, 0)

         if selection == 0:
                self.coins.append(GoldCoin())
                self.isGoldCoin = True
                self.isSilverCoin = False
         #else:
               # self.power_ups.append(SilverCoin())
                #self.isGoldCoin = False
               #self.isSilverCoin = True
        
      for coin in self.coins:
         if coin.used or coin.rect.x < -coin.rect.width:
           self.coins.pop()

         #if power_up.used:
           #player.set_power_up(power_up)
           
         coin.update(game_speed, player)

        

   def draw(self, screen):
     for coin in self.coins:
       coin.draw(screen)      