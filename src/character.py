from configuration import Config


class Character():
  def __init__(self, name, hp, mp, attack, spell):
    self.status_attack = attack
    self.name = name
    self.hp = hp
    self.mp = mp
    self.spell = spell

  def attack(self, target):
    target.reduce_hp(self.status_attack)

  def cast_spell(self, target, spell):
    # if(self.mp > self.spells[spell]["mp"]):
      self.mp -= self.spell[spell]["mp"]
      target.reduce_hp(self.spell[spell]["damage"])
  
  def reduce_hp(self, attack):
    if(self.hp > attack):
      self.hp -= attack
    else:
      self.hp = 0
    # print(self.name+" hp: %d, by character.reduce_hp()" % self.hp)
