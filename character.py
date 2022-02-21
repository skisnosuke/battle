from settings import Settings

class Character():
  def __init__(self, attack, name, hp, mp):
    self.settings = Settings()
    self.status_attack = attack
    self.name = name
    self.hp = hp
    self.mp = mp

  def attack(self, target):
    target.reduce_hp(self.status_attack)

  def incantation(self, target):
    if(self.mp > self.settings.mera):
      target.reduce_hp(settings.mera_damage)
      self.mp -= self.settings.mera
  
  def reduce_hp(self, attack):
    if(self.hp > attack):
      self.hp -= attack
    else:
      self.hp = 0
    print(self.name+" hp: %d, by character.reduce_hp()" % self.hp)
