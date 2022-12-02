from pygame import Rect, display, draw

from configuration import Config


class Log:
  def __init__(self, screen, font):
    self.screen = screen
    self.font = font

  def draw(self, message):
    draw.rect(self.screen, Config.log["border_color"], Rect(Config.log["window_coordinate"]+Config.log["window_size"]), Config.log["border_width"])
    draw.rect(self.screen, Config.log["window_color"], Rect(Config.log["window_coordinate"]+Config.log["window_size"]))

    self.text = self.font.render(message, False, Config.font["color"])
    self.screen.blit(self.text,
      (tuple(map(lambda n: n+16, Config.log["window_coordinate"]+Config.log["window_size"]))))
    display.flip()
