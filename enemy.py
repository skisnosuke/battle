import pygame
from pygame.locals import *
from settings import Settings

class Enemy:
    def __init__(self):
        self.settings = Settings()
        self.enemy_img = self.settings.enemy_img
        self.enemy_position = self.settings.enemy_position

    def draw(self, screen):
        # screen.blit(self.enemy_img, self.enemy_position, (210, 150, 170, 130))
        screen.blit(self.enemy_img, self.enemy_position)
        # screen.blit(self.enemy_img, self.enemy_position)