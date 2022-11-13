from pygame import Rect, draw

from configuration import Config


class Log:
  message_dict = {
      "appearance": "スライムが あらわれた！\nコマンド？",
      "attack": "ゆうしゃ の こうげき！\nスライムに 5ポイントの\nダメージを あたえた！",
      "spell": "コマンド？",
      "escape": "ゆうしゃは にげだした。\nしかし まわりこまれてしまった。",
      "tool": "どうぐ",
      "mera": "ゆうしゃ は メラ の\nじゅもんを となえた！"
    }
    # スライムを たおした！\nけいけんち 1ポイントをかくとく\n1ゴールドを てにいれた！

  def __init__(self):
    self.message = self.message_dict["appearance"]

  def set_message(self, key):
    self.message = self.message_dict[key]

  def draw(self, font, screen):
    draw.rect(screen, Config.log["border_color"], Rect(Config.log["window_coordinate"]+Config.log["window_size"]), Config.log["border_width"])
    draw.rect(screen, Config.log["window_color"], Rect(Config.log["window_coordinate"]+Config.log["window_size"]))

    self.text = font.render(self.message, False, Config.font["color"])
    screen.blit(self.text,
      (tuple(map(lambda n: n+16, Config.log["window_coordinate"]+Config.log["window_size"]))))

  #def draw_damage(self, damege):
    #self.text = self.settings.font.render("スライムに"+damage+"のダメージ")
    #screen.blit(self.text,
     #(tuple(map(lambda n: n+16, self.settings.log_position+self.settings.log_length))))
