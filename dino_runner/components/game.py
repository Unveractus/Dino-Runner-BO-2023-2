import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, MUSIC, DEAD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.cloud import CLOUD
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.coins.coin_manager import CoinManager

from dino_runner.components import text_utils

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(MUSIC)
pygame.mixer.music.play(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0
        self.y_pos_cloud = 100
        self.cloud_speed = 10
        self.player = Dinosaur()
        self.obstcle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.coin_manager = CoinManager()
        self.points = 0
        self.death_count = 0
        self.paused = False

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if self.paused == False:
                self.events()
                self.update()
                self.draw()
            else:
               text, text_rect = text_utils.get_message('Prees any key to start', 30)   
               self.screen.blit(text, text_rect)
               event = pygame.event.wait()
               if event.type == pygame.KEYDOWN:
                  self.paused = False
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True 
                self.reset()

#Actualiza estado de juego
    def update(self):
      if self.playing:
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_p] and self.paused == False:
           
           text, text_rect = text_utils.get_message('Prees any key to start', 30)   
           self.screen.blit(text, text_rect)
           self.paused = True
        else:
            self.player.update(user_input)
            self.obstcle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.coin_manager.update(self.game_speed,self.points,self.player)
            self.points += 1
            if self.points % 200 == 0:
                self.game_speed += 2 
            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1


    def draw(self):
      if self.paused == False:
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
      
        if self.playing:
            self.draw_background()
            self.draw_clouds()
            self.player.draw(self.screen)
            self.draw_score()
            self.draw_power_time(self.player)
            self.draw_coins(self.player)
            self.obstcle_manager.draw (self.screen)
            self.power_up_manager.draw(self.screen)
            self.coin_manager.draw(self.screen)
        else:
          self.draw_menu(self.player)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_clouds(self):
        image_width = CLOUD.get_width() 
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1000
        self.x_pos_cloud -= self.cloud_speed    
    
    def draw_coins(self, player):
        coins, coins_rect = text_utils.get_message('Coins:' + str(player.coins), 20, 1000, 70)
        self.screen.blit(coins, coins_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message('Points:' + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_rect)

    def draw_power_time(self, player):
        if player.shield:
         poweruptext, power_rect = text_utils.get_message('PowerTime: ' + str(player.time_to_show), 50, 200, 40)
         self.screen.blit(poweruptext, power_rect)    

    def draw_menu (self, player):
        white_color = (255, 255, 255) 
        self.screen.fill(white_color)
        self.print_menu_element(player)

    def print_menu_element(self, player):
        if self.death_count == 0:
         text, text_rect = text_utils.get_message('Prees any key to start', 30)   
         self.screen.blit(text, text_rect)
        else:
         text, text_rect = text_utils.get_message('Prees any key to restart', 30)   
         score, score_rect = text_utils.get_message('Your score is: ' + str(self.points), 30, height= SCREEN_HEIGHT // 2 + 50)   
         coins, coins_rect = text_utils.get_message('You collected: ' + str(player.coins) + ' dinocoins', 30, height= SCREEN_HEIGHT // 2 + 100 )   

         self.screen.blit(text, text_rect)
         self.screen.blit(score, score_rect)
         self.screen.blit(coins, coins_rect)

    
    def reset(self):
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0
        self.y_pos_cloud = 100
        self.cloud_speed = 10
        self.player = Dinosaur()
        self.obstcle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0