import pygame
from pygame.locals import *
from settings import Settings

class Command:
  def __init__(self):
    self.settings = Settings()
    self.action_selected = 0
  
  def act(self, player, target):
    if(self.action_selected == 0):  #たたかう
      player.attack(target)
    if(self.action_selected == 1):  #呪文
      player.cast_spell(target)

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), Rect(self.settings.command_position+self.settings.command_length), 10)
    pygame.draw.rect(screen, (0,0,0), Rect(self.settings.command_position+self.settings.command_length))

    actions = ["たたかう", "じゅもん", "にげる", "どうぐ"]
    action_texts = list(map(
      lambda action: self.settings.font.render(action, False, (255, 255, 255))
      , actions))
    screen.blit(action_texts[0], self.settings.command_action_position_upper_left)
    screen.blit(action_texts[1], self.settings.command_action_position_upper_right)
    screen.blit(action_texts[2], self.settings.command_action_position_lower_left)
    screen.blit(action_texts[3], self.settings.command_action_position_lower_right)

    cursor_positions = [
      (self.settings.command_action_position_upper_left[0]-18,
        self.settings.command_action_position_upper_left[1]),
      (self.settings.command_action_position_upper_right[0]-18,
        self.settings.command_action_position_upper_right[1]),
      (self.settings.command_action_position_lower_left[0]-18,
        self.settings.command_action_position_lower_left[1]),
      (self.settings.command_action_position_lower_right[0]-18,
        self.settings.command_action_position_lower_right[1]),
    ]
    cursor = self.settings.font.render("▶", False, (255, 255, 255))
    screen.blit(cursor, cursor_positions[self.action_selected])
    