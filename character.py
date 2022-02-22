from settings import Settings

class Character():
  def __init__(self, attack, name, hp, mp, spells):
    self.settings = Settings()
    self.status_attack = attack
    self.name = name
    self.hp = hp
    self.mp = mp
    self.spells = spells

  def attack(self, target):
    target.reduce_hp(self.status_attack)

  def cast_spell(self, target, spell):
    if(self.mp > self.spells[spell]["消費MP"]):
      self.mp -= self.spells[spell]["消費MP"]
      target.reduce_hp(self.spells[spell]["ダメージ"])
  
  def reduce_hp(self, attack):
    if(self.hp > attack):
      self.hp -= attack
    else:
      self.hp = 0
    print(self.name+" hp: %d, by character.reduce_hp()" % self.hp)
