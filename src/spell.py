from configuration import Config
from sound import Sound


class Spell:
  def __init__(self, key):
    self.label = Config.spell[key]["label"]
    self.mp = Config.spell[key]["mp"]
    self.type = Config.spell[key]["type"]
    self.effect = Config.spell[key]["effect"]
  
  def cast(self, caster, target):
    caster.reduce_mp(self.mp)
    Sound.play_cast_spell()
    if self.type == "offensive":
      target.reduce_hp(self.effect)
      return
    if self.type == "recovery":
      caster.heal_hp(self.effect)
      return
    
