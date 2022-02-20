import pygame
from pygame.locals import *
from settings import Settings
from command import Command
from character import Character

class Player(Character):
  def __init__(self):
    self.settings = Settings()
    super().__init__(self.settings.enemy_status_attack, self.settings.enemy_status_name, self.settings.enemy_status_hp, self.settings.enemy_status_mp)
    self.command = Command()
    self.font = self.settings.font
    self.status_attack = self.settings.player_status_attack
    self.name = self.settings.font.render(self.name, False, (255, 255, 255))
    self.level = self.settings.player_status_level

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), Rect(self.settings.player_position+self.settings.player_length), 10)
    pygame.draw.rect(screen, (0,0,0), Rect(self.settings.player_position+self.settings.player_length))

    hp = self.settings.font.render("ＨＰ{:6d}".format(self.hp), False, (255, 255, 255))
    mp = self.settings.font.render("ＭＰ{:6d}".format(self.mp), False, (255, 255, 255))
    level = self.settings.font.render("レベル{:4d}".format(self.level), False, (255, 255, 255))

    screen.blit(self.name, self.settings.player_status_name_position)
    screen.blit(level, self.settings.player_status_level_position)
    screen.blit(hp, self.settings.player_status_hp_position)
    screen.blit(mp, self.settings.player_status_mp_position)
    