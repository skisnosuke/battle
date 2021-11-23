import pygame
from pygame.locals import *
from settings import Settings
from character import Character
      # コマンド表示
      # 名前
      # Lv
      # HP
      # MP
class Player(Character):
  def __init__(self):
    self.settings = Settings()
    super().__init__(self.settings.player_status_attack, self.settings.player_status_hp, self.settings.player_status_name)
    self.name = self.settings.font.render(self.settings.player_status_name, False, (255, 255, 255))

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255),
      Rect(self.settings.player_position+self.settings.player_length), 10)
    pygame.draw.rect(screen, (0,0,0),
      Rect(self.settings.player_position+self.settings.player_length))
    screen.blit(self.name,
      tuple(map(lambda n: n+4, self.settings.player_position)))
