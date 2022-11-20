from pygame import Rect, display, draw

from configuration import Config
from cursor import Cursor
from sound import Sound


class Command:
  def __init__(self, screen, font):
    self.screen = screen
    self.font = font
    self.cursor = Cursor(screen, font)
    self.initial_options = [
        { "label": "たたかう", "id": "attack" }, { "label": "じゅもん", "id": "spells" },
        { "label": "にげる", "id": "escape" }, { "label": "どうぐ", "id": "tool" },
    ]
    self.options = self.initial_options

  def _let_attack(self, attacker, target):
    attacker.attack(target)
    
  def _let_cast_spell(self, caster, target, spell):
    caster.cast_spell(target, spell)

  def get_option_id(self):
    selected_idx = self.cursor.get_idx()
    return self.options[selected_idx]["id"]

  def move_cursor(self, key):
    self.cursor.move(len(self.options), key)
    self.draw()

  def go_back(self):
    self.options = self.initial_options
    self.draw()
  
  def execute(self, player, enemy, log):
    option_idx = self.cursor.get_idx()
    option_id = self.options[option_idx]["id"]
    if option_id == "attack":
      self._let_attack(player, enemy)
      log.draw(player.name + " の こうげき！\n" + enemy.name + "に 5ポイントの\nダメージ！")
      Sound.play_attack()
    elif option_id == "spells":
      self.options = [{"id": "spell", "name": key, "label": value.label} for key, value in player.spell.items()]
    elif option_id == "spell":
      spell_label = self.options[option_idx]["label"]
      log.draw(player.name + " は " + spell_label + " の\nじゅもんを となえた！")
      spell_name = self.options[option_idx]["name"]
      player.cast_spell(spell_name, enemy)
      log.draw(enemy.name + " に " + str(player.spell[spell_name].get_effect()) + " ポイントの\nダメージ！")
    elif option_id == "escape":
      log.draw(player.name + " は にげだした。\nしかし まわりこまれてしまった。")
      Sound.play_escape()
    self.draw()

  def draw(self):
    draw.rect(self.screen, Config.command["border_color"], Rect((Config.command["window_coordinate"]+Config.command["window_size"])), Config.command["border_width"])
    draw.rect(self.screen, Config.command["window_color"], Rect(Config.command["window_coordinate"]+Config.command["window_size"]))
    for idx in range(len(self.options)):
      label = self.font.render(self.options[idx]["label"], False, Config.font["color"])
      self.screen.blit(label, Config.command["option_coordinates"][idx])
    self.cursor.draw()
    display.flip()
