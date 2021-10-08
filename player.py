import pygame
from pygame.locals import *
from settings import Settings
      # コマンド表示
      # 名前
      # Lv
      # HP
      # MP
class Player():
  def __init__(self):
    self.settings = Settings()
    self.player_position = self.settings.player_position
    self.name = self.settings.font.render("ゆうしゃ", False, (255, 255, 255))

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255),
      Rect(self.settings.player_position+self.settings.player_length), 10)
    pygame.draw.rect(screen, (0,0,0),
      Rect(self.settings.player_position+self.settings.player_length))
    screen.blit(self.name,
      tuple(map(lambda n: n+8, self.settings.player_position+self.settings.player_length)))