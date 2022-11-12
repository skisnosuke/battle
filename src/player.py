from pygame import Rect, draw

from character import Character
from configuration import Config


class Player(Character):
  def __init__(self, level, name, hp, mp, attack, spell):
    super().__init__(name, hp, mp, attack, spell)
    self.level = level

  def draw(self, font, screen):
    draw.rect(screen, Config.player["border_color"], Rect(Config.player["window_coordinate"]+Config.player["window_size"]), Config.player["border_width"])
    draw.rect(screen, Config.player["window_color"], Rect(Config.player["window_coordinate"]+Config.player["window_size"]))

    name = font.render(self.name, False, Config.font["color"])
    hp = font.render("ＨＰ{:6d}".format(self.hp), False, Config.font["color"])
    mp = font.render("ＭＰ{:6d}".format(self.mp), False, Config.font["color"])
    level = font.render("レベル{:4d}".format(self.level), False, Config.font["color"])

    screen.blit(name, Config.player["name_coordinate"])
    screen.blit(level, Config.player["level_coordinate"])
    screen.blit(hp, Config.player["hp_coordinate"])
    screen.blit(mp, Config.player["mp_coordinate"])
