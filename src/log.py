import pygame
from pygame.locals import *
from settings import Settings

class Log:
  def __init__(self):
    self.settings = Settings()
    self.font = self.settings.font
    self.__action_selected = "init"

  def change_action_selected(self, key):
    self.__action_selected = key

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), 
      Rect(self.settings.log_position+self.settings.log_length), 10)
    pygame.draw.rect(screen, (0,0,0),
      Rect(self.settings.log_position+self.settings.log_length))

    # たたかう じゅもん にげる どうぐ
    messages = {
      "init": "スライムが あらわれた！\nコマンド？",
      "attack": "ゆうしゃ の こうげき！\nスライムに 5ポイントの\nダメージを あたえた！",
      "spell": "コマンド？",
      "escape": "ゆうしゃは にげだした。\nしかし まわりこまれてしまった。",
      "tool": "どうぐ",
    }
    # スライムを たおした！\nけいけんち 1ポイントをかくとく\n1ゴールドを てにいれた！
    # ゆうしゃ は メラ の\nじゅもんを となえた！

    self.text = self.settings.font.render(messages[self.__action_selected], False, (255, 255, 255))
    screen.blit(self.text,
      (tuple(map(lambda n: n+16, self.settings.log_position+self.settings.log_length))))

  #def draw_damage(self, damege):
    #self.text = self.settings.font.render("スライムに"+damage+"のダメージ")
    #screen.blit(self.text,
     #(tuple(map(lambda n: n+16, self.settings.log_position+self.settings.log_length))))
