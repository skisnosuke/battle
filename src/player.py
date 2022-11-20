from pygame import Rect, display, draw

from character import Character
from configuration import Config


class Player(Character):
  def __init__(self, screen, font, name, level, hp, mp, attack, spells):
    self.screen = screen
    self.font = font
    super().__init__(name, hp, mp, attack, spells)
    self.level = level
  
  def reduce_hp(self, attack):
    super().reduce_hp(attack)
    self.draw()
  
  def heal_hp(self, heal):
    super().heal_hp(heal)
    self.draw()
  
  def reduce_mp(self, cost):
    super().reduce_mp(cost)
    self.draw()

  def draw(self):
    draw.rect(self.screen, Config.player["border_color"], Rect(Config.player["window_coordinate"]+Config.player["window_size"]), Config.player["border_width"])
    draw.rect(self.screen, Config.player["window_color"], Rect(Config.player["window_coordinate"]+Config.player["window_size"]))

    name = self.font.render(self.name, False, Config.font["color"])
    hp = self.font.render("ＨＰ{:6d}".format(self.hp), False, Config.font["color"])
    mp = self.font.render("ＭＰ{:6d}".format(self.mp), False, Config.font["color"])
    level = self.font.render("レベル{:4d}".format(self.level), False, Config.font["color"])

    self.screen.blit(name, Config.player["name_coordinate"])
    self.screen.blit(level, Config.player["level_coordinate"])
    self.screen.blit(hp, Config.player["hp_coordinate"])
    self.screen.blit(mp, Config.player["mp_coordinate"])

    display.flip()
