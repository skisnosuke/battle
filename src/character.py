from spell import Spell


class Character():
  def __init__(self, name, hp, mp, attack, spells):
    self.status_attack = attack
    self.name = name
    self.hp = hp
    self.mp = mp
    self.spells = spells

  def attack(self, target):
    target.reduce_hp(self.status_attack)

  def cast_spell(self, target, spell):
    #TODO Spellクラスを使う
    mp_cost = Spell.get_mp(spell)
    if(self.mp > mp_cost):
      self.mp -= mp_cost
      target.reduce_hp(Spell.get_damage[spell])
  
  def reduce_hp(self, attack):
    if(self.hp > attack):
      self.hp -= attack
    else:
      self.hp = 0
    # print(self.name+" hp: %d, by character.reduce_hp()" % self.hp)
