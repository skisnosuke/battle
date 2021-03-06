from pygame.locals import *
from settings import Settings
from character import Character

class Enemy(Character):
    def __init__(self):
        self.settings = Settings()
        super().__init__(self.settings.enemy_status_attack, 
                         self.settings.enemy_status_name, 
                         self.settings.enemy_status_hp, 
                         self.settings.enemy_status_mp, 
                         self.settings.player_spells)

    def draw(self, screen):
        screen.blit(self.settings.enemy_bg_img, self.settings.enemy_bg_img_position)
        screen.blit(self.settings.enemy_img, self.settings.enemy_position)

    def attacked(self, damage):
        self.enemy_hp -= damage
