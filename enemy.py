import pygame
from pygame.locals import *
from settings import Settings

class Enemy:
    def __init__(self):
        self.settings = Settings()

        self.enemy_hp = self.settings.enemy_hp

    def draw(self, screen):
        screen.blit(self.settings.enemy_bg_img, self.settings.enemy_bg_img_position)
        screen.blit(self.settings.enemy_img, self.settings.enemy_position)

    def attacked(self, damage):
        self.enemy_hp -= damage