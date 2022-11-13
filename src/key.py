from pygame import (K_BACKSPACE, K_DOWN, K_LEFT, K_RETURN, K_RIGHT, K_SPACE,
                    K_UP)


class Key:
  table = {
    K_UP: "move" , K_DOWN: "move" , K_LEFT: "move" , K_RIGHT: "move" ,
    K_RETURN: "select" , K_BACKSPACE: "go_back" , K_SPACE: "select"
  }

  @staticmethod
  def get(self, id):
    self.table[id]

  @staticmethod
  def is_valid_key(self, key):
    key in self.table.keys()

  @staticmethod
  def should_cursor_move(self, key):
    return key in self.table[key] == "move"

  @staticmethod
  def should_command_execute(self, key):
    return key in self.table[key] == "select"

  @staticmethod
  def should_go_back(self, key):
    return key in self.table[key] == "go_back"


