from pygame import Rect, draw

from configuration import Config


class Log:
  def __init__(self, enemy):
    self.message = enemy + "が あらわれた！\nコマンド？"

  def set_message(self, msg):
    self.message = msg

  def draw(self, font, screen):
    draw.rect(screen, Config.log["border_color"], Rect(Config.log["window_coordinate"]+Config.log["window_size"]), Config.log["border_width"])
    draw.rect(screen, Config.log["window_color"], Rect(Config.log["window_coordinate"]+Config.log["window_size"]))

    self.text = font.render(self.message, False, Config.font["color"])
    screen.blit(self.text,
      (tuple(map(lambda n: n+16, Config.log["window_coordinate"]+Config.log["window_size"]))))
