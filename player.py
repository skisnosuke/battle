import pygame
from pygame.locals import *
from settings import Settings
from command import Command
from character import Character
      # コマンド表示
      # 名前
      # Lv
      # HP
      # MP
class Player(Character):
  def __init__(self):
    self.settings = Settings()
    self.command = Command()
    self.name = self.settings.font.render("ゆうしゃ", False, (255, 255, 255))
    self.status_attack = self.settings.status_attack
    self.font = pygame.font.Font(None, 35)

  #def attack(self):
    #self.remain_enemy_hp = self.command.enemy_hp - self.command.attacked

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255),
      Rect(self.settings.player_position+self.settings.player_length), 10)
    pygame.draw.rect(screen, (0,0,0),
      Rect(self.settings.player_position+self.settings.player_length))
    str_hp = "HP : {:02}".format(self.settings.status_hp)
    str_mp = "MP : {:01}".format(self.settings.status_mp)
    str_lv = "LV : {:01}".format(self.settings.status_lv)

    name = self.settings.font.render(self.settings.status_name, True, (255, 255, 255))
    hp = self.font.render(str_hp, True, (255, 255, 255))
    mp = self.font.render(str_mp,True, (255, 255, 255))
    level = self.font.render(str_lv, True, (255, 255, 255))
    screen.blit(name, [40, 20])
    screen.blit(hp, [40, 70])
    screen.blit(mp, [40, 110])
    screen.blit(level, [40, 150])
   # tuple(map(lambda n: n+4, self.settings.player_position)))
