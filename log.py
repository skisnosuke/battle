import pygame
from pygame.locals import *
from settings import Settings

class Log:
  def __init__(self):
    self.settings = Settings()
    self.text = self.settings.font.render("スライムが あらわれた！", False, (255, 255, 255))

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), 
      Rect(self.settings.log_position+self.settings.log_length), 10)
    pygame.draw.rect(screen, (0,0,0),
      Rect(self.settings.log_position+self.settings.log_length))
    screen.blit(self.text,
      (tuple(map(lambda n: n+16, self.settings.log_position+self.settings.log_length))))
  
