from pygame import Rect, draw

from configuration import Config


class Log:
  def __init__(self):
    self.__action_selected = "init"

  def change_action_selected(self, key):
    self.__action_selected = key

  def draw(self, font, screen):
    draw.rect(screen, Config.log["border_color"], Rect(Config.log["window_coordinate"]+Config.log["window_size"]), Config.log["border_width"])
    draw.rect(screen, Config.log["window_color"],Rect(Config.log["window_coordinate"]+Config.log["window_size"]))

    # たたかう じゅもん にげる どうぐ
    messages = {
      "init": "スライムが あらわれた！\nコマンド？",
      "attack": "ゆうしゃ の こうげき！\nスライムに 5ポイントの\nダメージを あたえた！",
      "spell": "コマンド？",
      "escape": "ゆうしゃは にげだした。\nしかし まわりこまれてしまった。",
      "tool": "どうぐ",
      "mera": "ゆうしゃ は メラ の\nじゅもんを となえた！"
    }
    # スライムを たおした！\nけいけんち 1ポイントをかくとく\n1ゴールドを てにいれた！

    self.text = font.render(messages[self.__action_selected], False, Config.font["color"])
    screen.blit(self.text,
      (tuple(map(lambda n: n+16, Config.log["window_coordinate"]+Config.log["window_size"]))))

  #def draw_damage(self, damege):
    #self.text = self.settings.font.render("スライムに"+damage+"のダメージ")
    #screen.blit(self.text,
     #(tuple(map(lambda n: n+16, self.settings.log_position+self.settings.log_length))))
