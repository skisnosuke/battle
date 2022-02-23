from ..character import Character

passed = 0
failed = 0

print("こうげき")
player = Character(10, "p", 1, 0) # (attack, name, hp, mp)
enemy = Character(0, "e", 10, 0) # (attack, name, hp, mp)
player.attack(enemy)
result = enemy.hp
if(result == 0):
  print("Passed")
  passed += 1
else:
  print("Error result: %d" % result)
  failed += 1

print("呪文")
# ここから書く

print("Passed: %d, Failed: %d" % (passed, failed))
