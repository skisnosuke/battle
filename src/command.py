from pygame import (K_BACKSPACE, K_DOWN, K_LEFT, K_RETURN, K_RIGHT, K_SPACE,
                    K_UP, Rect, draw)

from configuration import Config
from sound import Sound


class Command:
  def __init__(self):
    self.selected_idx = 0
    # |0 1|
    # |2 3|
    self.options = [
      { "label": "たたかう", "id": "attack" }, { "label": "じゅもん", "id": "spell" },
      { "label": "にげる", "id": "escape" }, { "label": "どうぐ", "id": "tool" },
    ]

  def _let_attack(self, attacker, target):
    attacker.attack(target)
    
  def _let_cast_spell(self, caster, target, spell):
    caster.cast_spell(target, spell)

  def _move_cursor(self):
    return 0

  def check_key_event(self, key, player, enemy, log):
      num_of_actions = len(self.options)
      if key == K_UP:
          self.selected_idx = (
              (self.selected_idx - 2) % num_of_actions )
          Sound.play_cursor()

      elif key == K_RIGHT or key == K_LEFT:
          self.selected_idx = (
              self.selected_idx + 1
                if self.selected_idx % 2 == 0
                  and self.selected_idx + 1 < num_of_actions
                else self.selected_idx - 1 )
          Sound.play_cursor()
      elif key == K_DOWN:
              self.selected_idx = (
                  (self.selected_idx + 2) % num_of_actions )
              Sound.play_cursor()
      elif key == K_RETURN or key == K_SPACE:
          Sound.play_cursor()
          selected_option_id = self.options[self.selected_idx]["id"]
          if selected_option_id == "attack":
              self._let_attack(player, enemy)
              Sound.play_attack()
          elif selected_option_id == "spell":
              self.option = player.spell
          elif selected_option_id == "escape":
              Sound.play_escape()
          else:
              self._let_cast_spell(player, enemy, selected_option_id)
              Sound.play_cast_spell()
      elif key == K_BACKSPACE:
        self.options = [
          { "label": "たたかう", "id": "attack" }, { "label": "じゅもん", "id": "spell" },
          { "label": "にげる", "id": "escape" }, { "label": "どうぐ", "id": "tool" },
        ]

  def draw(self, font, screen):
    draw.rect(screen, Config.command["border_color"], Rect((Config.command["window_coordinate"]+Config.command["window_size"])), Config.command["border_width"])
    draw.rect(screen, Config.command["window_color"], Rect(Config.command["window_coordinate"]+Config.command["window_size"]))

    for idx in range(len(self.options)):
      label = font.render(self.options[idx]["label"], False, Config.font["color"])
      screen.blit(label, Config.command["option_coordinates"][idx])

    cursor = font.render("▶", False, Config.font["color"])
    screen.blit(cursor, Config.command["cursor_coordinates"][self.selected_idx])
    