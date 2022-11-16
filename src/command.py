from pygame import Rect, draw

from configuration import Config
from cursor import Cursor
from sound import Sound


class Command:
  def __init__(self):
    self.cursor = Cursor()
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

  def go_back(self):
    self.options = self.initial_options
  
  def execute(self, player, enemy, log):
    option_idx = self.cursor.get_idx()
    option_id = self.options[option_idx]["id"]
    if option_id == "attack":
      self._let_attack(player, enemy)
      log.set_message(player.name + " の こうげき！\n" + enemy.name + "に 5ポイントの\nダメージ！")
      Sound.play_attack()
      return
    if option_id == "spells":
      self.options = [{"id": "spell", "name": key, "label": value.label} for key, value in player.spell.items()]
      return
    if option_id == "spell":
      spell_name = self.options[option_idx]["name"]
      player.cast_spell(spell_name, enemy)
      spell_label = self.options[option_idx]["label"]
      log.set_message(player.name + " は " + spell_label + " の\nじゅもんを となえた！")
      return
    if option_id == "escape":
      log.set_message(player.name + " は にげだした。\nしかし まわりこまれてしまった。")
      Sound.play_escape()
      return

  def draw(self, font, screen):
    draw.rect(screen, Config.command["border_color"], Rect((Config.command["window_coordinate"]+Config.command["window_size"])), Config.command["border_width"])
    draw.rect(screen, Config.command["window_color"], Rect(Config.command["window_coordinate"]+Config.command["window_size"]))

    for idx in range(len(self.options)):
      label = font.render(self.options[idx]["label"], False, Config.font["color"])
      screen.blit(label, Config.command["option_coordinates"][idx])
    
    self.cursor.draw(font, screen)
