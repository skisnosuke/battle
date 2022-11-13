from pygame import Rect, draw

from configuration import Config
from cursor import Cursor
from sound import Sound
from spell import Spell


class Command:
  def __init__(self):
    self.cursor = Cursor()
    self.default_options = [
        { "label": "たたかう", "id": "attack" }, { "label": "じゅもん", "id": "spell" },
        { "label": "にげる", "id": "escape" }, { "label": "どうぐ", "id": "tool" },
    ]
    self.options = self.default_options

  def _let_attack(self, attacker, target):
    attacker.attack(target)
    
  def _let_cast_spell(self, caster, target, spell):
    caster.cast_spell(target, spell)

  def get_option_id(self):
    selected_idx = self.cursor.get_idx()
    return self.options[selected_idx]["id"]

  def move_cursor(self, key):
    self.cursor.move(key)

  def go_back(self):
    self.options = self.default_options
  
  def execute(self, player, enemy):
    option_idx = self.cursor.get_idx()
    option_id = self.options[option_idx]["id"]
    if option_id == "attack":
        self._let_attack(player, enemy)
        Sound.play_attack()
    elif option_id == "spell":
        self.options = [{"id": id, "label": Spell.get_label(id)} for id in player.spells]
    elif option_id == "escape":
        Sound.play_escape()
    else:
        self._let_cast_spell(player, enemy, option_id)
        Sound.play_cast_spell()
    return

  def draw(self, font, screen):
    draw.rect(screen, Config.command["border_color"], Rect((Config.command["window_coordinate"]+Config.command["window_size"])), Config.command["border_width"])
    draw.rect(screen, Config.command["window_color"], Rect(Config.command["window_coordinate"]+Config.command["window_size"]))

    for idx in range(len(self.options)):
      label = font.render(self.options[idx]["label"], False, Config.font["color"])
      screen.blit(label, Config.command["option_coordinates"][idx])
    
    self.cursor.draw(font, screen)
