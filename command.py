import pygame
from pygame.locals import *
from settings import Settings

class Command:
    #   たたかう じゅもん にげる どうぐ
  def __init__(self):
    self.settings = Settings()
    self.command_position = self.settings.command_position

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), Rect(self.settings.command_position), 10)
    pygame.draw.rect(screen, (0,0,0), Rect(self.settings.command_position))