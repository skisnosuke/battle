import pygame
from pygame.locals import *
from settings import Settings

class Enemy:
    def __init__(self):
        self.settings = Settings()

    def draw(self, screen):
        screen.blit(self.settings.enemy_bg_img, self.settings.enemy_bg_img_position)
        screen.blit(self.settings.enemy_img, self.settings.enemy_position)