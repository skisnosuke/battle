import pygame
from pygame.locals import *
from settings import Settings
from command import Command
from character import Character

class Player(Character):
  def __init__(self):
    self.settings = Settings()
    self.command = Command()
    self.font = self.settings.font
    self.name = self.settings.font.render(self.settings.player_status_name, False, (255, 255, 255))
    self.status_attack = self.settings.player_status_attack

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255),Rect(self.settings.player_position+self.settings.player_length), 10)
    pygame.draw.rect(screen, (0,0,0),Rect(self.settings.player_position+self.settings.player_length))
    str_lv = "レベル{:4d}".format(self.settings.player_status_lv)
    str_hp = "ＨＰ{:6d}".format(self.settings.player_status_hp)
    str_mp = "ＭＰ{:6d}".format(self.settings.player_status_mp)

    name = self.settings.font.render(self.settings.player_status_name, True, (255, 255, 255))
    hp = self.settings.font.render(str_hp, True, (255, 255, 255))
    mp = self.settings.font.render(str_mp,True, (255, 255, 255))
    level = self.settings.font.render(str_lv, True, (255, 255, 255))
    screen.blit(name, [40, 20])
    screen.blit(level, [40, 70])
    screen.blit(hp, [40, 110])
    screen.blit(mp, [40, 150])
   # tuple(map(lambda n: n+4, self.settings.player_position)))
