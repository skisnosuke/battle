import sys
sys.path.append("src")
from unittest import TestCase, main
from character import Character # vscode上で警告出るが無視

class Test(TestCase):
  def test_example(self): # メソッド名は必ずtest_で始める
    actual = 1 + 1 # 実行結果を代入
    expected = 2 # 期待する値
    self.assertEqual(expected, actual) # 等しければPassed

  def test_player_attack_reduces_enemy_hp_by_player_status_attack(self):
    # 主人公の攻撃力の分だけ敵のHPが減る
    player = Character(10, "p", 1, 0) # (attack, name, hp, mp)
    enemy = Character(0, "e", 10, 0) # (attack, name, hp, mp)
    player.attack(enemy)
    actual = enemy.hp
    expected = 0
    self.assertEqual(expected, actual)

  def test_player_cast_spell_reduce_enemy_hp_by_mera_damage(self):
    player = Character(0, "p", 1, 10)
    enemy = Character(0, "e", 10, 0)
    player.cast_spell(enemy, "mera")
    actual = enemy.hp
    expected = 0
    self.assertEqual(expected, actual)
  
if __name__ == "__main__":
  main()