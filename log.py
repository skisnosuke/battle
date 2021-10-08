import pygame
from pygame.locals import *
from settings import Settings

class Log:
  #   〇〇が あらわれた！
  #   〇〇 の こうげき！
  def __init__(self):
    self.settings = Settings()
    self.text = self.settings.font.render("こんにちは", False, (255, 255, 255))
    self.log_position = self.settings.log_position

  def display(self, screen):
    screen.blit(self.text, (100, 100))

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), Rect(self.settings.log_position), 10)
    pygame.draw.rect(screen, (0,0,0), Rect(self.settings.log_position))
  
