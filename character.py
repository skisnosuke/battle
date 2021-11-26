class Character():
  def __init__(self, attack, hp, name):
    self.__status_attack = attack
    self.__status_hp = hp
    self.__status_name = name

  def attack(self, target):
    target.reduce_hp(self.__status_attack)
  
  def reduce_hp(self, attack):
    if(self.__status_hp >= attack):
      self.__status_hp -= attack
    else:
      self.__status_hp = 0
    print(self.__status_name+" hp: %d, by character.reduce_hp()" % self.__status_hp)
