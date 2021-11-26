class Character():
  def __init__(self, attack, hp, name):
    self.settings.player_status_attack = attack
    self.settings.enemy_status_hp = hp
    self.settings.enemy_status_name = name

  def attack(self, target):
    target.reduce_hp(self.settings.enemy_status_attack)
  
  def reduce_hp(self, attack):
    if(self.settings.enemy_status_hp >= attack):
      self.settings.enemy_status_hp -= attack
    else:
      self.settings.enemy_status_hp = 0
    print(self.settings.enemy_status_name+" hp: %d, by character.reduce_hp()" % self.settings.enemy_status_hp)
