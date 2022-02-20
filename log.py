import pygame
from pygame.locals import *
from settings import Settings

class Log:
  def __init__(self):
    self.settings = Settings()
    self.font = self.settings.font
    self.text = self.font.render("スライムが あらわれた！", False, (255, 255, 255))
    self.__action_idx = 0

  def change_action_idx(self, idx):
    self.__action_idx = idx

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), 
      Rect(self.settings.log_position+self.settings.log_length), 10)
    pygame.draw.rect(screen, (0,0,0),
      Rect(self.settings.log_position+self.settings.log_length))

    # たたかう じゅもん にげる どうぐ
    messages = [
      "ゆうしゃの こうげき！",
      "ゆうしゃは 呪文を唱えた",
      "ゆうしゃは にげだした。\nしかし まわりこまれてしまった。",
      "どうぐ",
    ]
    self.text = self.settings.font.render(messages[self.__action_idx], False, (255, 255, 255))
    screen.blit(self.text,
      (tuple(map(lambda n: n+16, self.settings.log_position+self.settings.log_length))))
