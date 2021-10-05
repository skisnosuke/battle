import pygame
from settings import Settings

class Log:
  #   〇〇が あらわれた！
  #   〇〇 の こうげき！
  def __init__(self):
    self.settings = Settings()
    self.font = pygame.font.Font(self.settings.font_name, 20)
    self.text = self.font.render("こんにちは", False, (255, 255, 255))

  def display(self, screen):
    screen.blit(self.text, (100, 100))
  
