from error import NotEnoughMpError
from spell import Spell


class Character():
  def __init__(self, name, hp, mp, attack, spells):
    self.status_attack = attack
    self.name = name
    self.hp = hp
    self.max_hp = hp
    self.mp = mp
    self.spell = {spell: Spell(spell) for spell in spells}

  def attack(self, target):
    target.reduce_hp(self.status_attack)

  def cast_spell(self, spell, target):
    self.spell[spell].cast(self, target)
  
  def reduce_hp(self, attack):
    if(self.hp >= attack):
      self.hp -= attack
    else:
      self.hp = 0
  
  def heal_hp(self, heal):
    if(self.hp + heal <= self.max_hp):
      self.hp += heal
    else:
      self.hp = self.max_hp
  
  def reduce_mp(self, cost):
    if(self.mp >= cost):
      self.mp -= cost
    else:
      raise NotEnoughMpError("Not enough MP")
