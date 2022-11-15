from pygame import (K_BACKSPACE, K_DOWN, K_LEFT, K_RETURN, K_RIGHT, K_SPACE,
                    K_UP)


class Key:
  table = {
    K_UP: "move" , K_DOWN: "move" , K_LEFT: "move" , K_RIGHT: "move" ,
    K_RETURN: "select" , K_BACKSPACE: "go_back" , K_SPACE: "select"
  }

  @staticmethod
  def is_valid_key(key):
    return key in Key.table.keys()

  @staticmethod
  def should_cursor_move(key):
    return Key.table[key] == "move"

  @staticmethod
  def should_command_execute(key):
    return Key.table[key] == "select"

  @staticmethod
  def should_go_back(key):
    return Key.table[key] == "go_back"


