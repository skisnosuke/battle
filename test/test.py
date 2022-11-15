import sys

sys.path.append("../src")
from unittest import TestCase, main

from pygame import init

from character import Character


class Test(TestCase):
  init()
  def test_example(self): # メソッド名は必ずtest_で始める
    actual = 1 + 1 # 実行結果を代入
    expected = 2 # 期待する値
    self.assertEqual(expected, actual) # 等しければPassed

  def test_player_attack_reduces_enemy_hp_by_player_status_attack(self):
    # 主人公の攻撃力の分だけ敵のHPが減る
    player = Character("hero", 1, 0, 10, []) # (name, hp, mp, attack, spells)
    enemy = Character("monster", 10, 0, 0, []) # (name, hp, mp, attack, spells)
    player.attack(enemy)
    actual = enemy.hp
    expected = 0
    self.assertEqual(expected, actual)

  def test_player_cast_spell_reduces_enemy_hp_by_mera_damage(self):
    # メラのダメージだけ敵のHPが減る
    # "mera": { "label": "メラ", "mp": 2, "type": "offensive", "effect": 10 },
    player = Character("hero", 1, 10, 0, ["mera"]) # (name, hp, mp, attack, spells)
    enemy = Character("monster", 10, 0, 0, []) # (name, hp, mp, attack, spells)
    player.cast_spell("mera", enemy)
    actual = enemy.hp
    expected = 0
    self.assertEqual(expected, actual)

  def test_player_cast_spell_reduces_players_mp_by_mera_cosume(self):
    # メラの消費mpだけプレイヤーのmpが減る
    # "mera": { "label": "メラ", "mp": 2, "type": "offensive", "effect": 10 },
    player = Character("hero", 1, 2, 0, ["mera"]) # (name, hp, mp, attack, spells)
    enemy = Character("monster", 10, 0, 0, []) # (name, hp, mp, attack, spells)
    player.cast_spell("mera", enemy)
    actual = player.mp
    expected = 0
    self.assertEqual(expected, actual)

  

if __name__ == "__main__":
  main()
