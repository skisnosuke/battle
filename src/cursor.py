from pygame import K_DOWN, K_LEFT, K_RIGHT, K_UP

from configuration import Config


class Cursor:
  def __init__(self, screen, font):
    self.screen = screen
    self.font = font
    self.idx = 0
    # |0 1|
    # |2 3|
    self.transition = [
      {
        0: { K_LEFT: 0, K_RIGHT: 0, K_UP: 0, K_DOWN: 0 },
      }, {
        0: { K_LEFT: 1, K_RIGHT: 1, K_UP: 0, K_DOWN: 0 },
        1: { K_LEFT: 0, K_RIGHT: 0, K_UP: 1, K_DOWN: 1 },
      }, {
        0: { K_LEFT: 1, K_RIGHT: 1, K_UP: 2, K_DOWN: 2 },
        1: { K_LEFT: 0, K_RIGHT: 0, K_UP: 2, K_DOWN: 2 },
        2: { K_LEFT: 0, K_RIGHT: 1, K_UP: 0, K_DOWN: 0 },
      }, {
        0: { K_LEFT: 1, K_RIGHT: 1, K_UP: 2, K_DOWN: 2 },
        1: { K_LEFT: 0, K_RIGHT: 0, K_UP: 3, K_DOWN: 3 },
        2: { K_LEFT: 3, K_RIGHT: 3, K_UP: 0, K_DOWN: 0 },
        3: { K_LEFT: 2, K_RIGHT: 2, K_UP: 1, K_DOWN: 1 },
      }
    ]
  
  def get_idx(self):
    return self.idx

  def move(self, len, key):
    self.idx = self.transition[len-1][self.idx][key]

  def draw(self):
    cursor = self.font.render("▶", False, Config.font["color"])
    self.screen.blit(cursor, Config.cursor["coordinates"][self.idx])

  

  
